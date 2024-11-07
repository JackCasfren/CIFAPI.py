import sys, os, http.client, json
sys.path.append(os.path.abspath('API_project'))
import creds
from datetime import datetime, timedelta
api_key = creds.api_key


def get_pantry_data():
    #print("get_pantry_data called")
    conn = http.client.HTTPSConnection("getpantry.cloud")
    payload = "" 
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("GET", f"/apiv1/pantry/{api_key}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    
    return data.decode("utf-8")


def update_pantry_account( name, description):
    conn = http.client.HTTPSConnection("getpantry.cloud")
    payload = json.dumps({
        "name": name,
        "description": description
    })
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("PUT", f"/apiv1/pantry/{api_key}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

# Example usage:
# result = update_pantry_account("Name of the pantry", "Description")
# print(result)


def list_all_baskets():
    print("The baskets are:")
    data = json.loads(get_pantry_data())
    baskets = data['baskets']
    for basket in baskets:
                    print(basket)

'''
# todo Make a funciton that formats the get_pantry_data 
 so it can be readable via CLI.
 And so it has the ttl time to days instead of unix time.
'''
def get_pantry_data_format():
    # Get the data
    json_string = get_pantry_data()

    """
    Make a get_pantry_data call but it is formated so it looks good on the CLI.    
    Use: just put it inside a print statement to dispay the pantry list and any errors.
    Returns:
        str: Formatted string ready for terminal display
    """
    try:
        # Parse the JSON string
        data = json.loads(json_string)
        
        # Create the formatted output
        output = []
        
        # Main info section
        output.append("=== PANTRY INFORMATION ===")
        output.append(f"Name: {data['name']}")
        output.append(f"Description: {data['description']}")
        output.append(f"Notifications: {'Enabled' if data['notifications'] else 'Disabled'}")
        output.append(f"Storage Usage: {data['percentFull']}%")
        
        # Get every single element from the list
        # We require this list to verify if the basket can be found in a error.
        # There is a bug where a error appears saying the basket does not exist when infact it does.
        basket_names = {basket['name'] for basket in data['baskets']}
        
        # Errors section with validation
        if data['errors']:
            output.append("\n=== ERRORS ===")
            for error in data['errors']:
                # Check if error mentions a basket that actually exists
                is_inconsistent = any(basket_name in error and basket_name in basket_names 
                                    for basket_name in basket_names)
                if is_inconsistent:
                    # this should not appear if it is not a error.
                    output.append(f"⚠️ {error} (Warning: Inconsistent error - basket exists)")

                else:
                    output.append(f"❌ {error}")
        
        # Baskets section
        if data['baskets']:
            output.append("\n=== BASKETS ===")
            # Sort baskets by TTL for better readability
            sorted_baskets = sorted(data['baskets'], key=lambda x: x['ttl'], reverse=True)
            
            for basket in sorted_baskets:
                # Convert TTL to readable time remaining
                ttl_delta = timedelta(seconds=basket['ttl'])
                days = ttl_delta.days
                hours = ttl_delta.seconds // 3600
                minutes = (ttl_delta.seconds % 3600) // 60
                
                output.append(f"\n📦 Basket: {basket['name']}")
                output.append(f"   Time remaining: {days}d {hours}h {minutes}m")
        
        return "\n".join(output)
    
    except json.JSONDecodeError:
        return "Error: Invalid JSON string"
    except KeyError as e:
        return f"Error: Missing required field {str(e)}"
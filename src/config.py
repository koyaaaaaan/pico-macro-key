# True:use lock pin 
# False:lock screen skipped
uselock = True

# lock pin(array) 
# 1:Button1 2:Button2 3:Button3
lockpin = [1,2,3,1,2,3]

# True: use tiny buzzer when waking up and pin succeeded
# False silent
buzzer = True

# Key board Layout Type
# en:US key layout 
# jp:Japanese key layout
layoutType = "jp"

# enabled > True:use section False:skip section
# data > Display label and key config (array 3)
#   label > Display label
#   value > String value it send to PC when it pressed 
keymap = [
           { "enabled": True,
             "data": [
               { "label": "Custom Label01", "value": "Key Input value01" },
               { "label": "Custom Label02", "value": "Key Input value02" },
               { "label": "Custom Label03", "value": "Key Input value03" }	
             ]
           },
           { "enabled": True,
             "data": [
               { "label": "Custom Label04", "value": "Key Input value04" },
               { "label": "Custom Label05", "value": "Key Input value05" },
               { "label": "Custom Label06", "value": "Key Input value06" }	
             ]
           },
           { "enabled": True,
             "data": [
               { "label": "Custom Label07", "value": "Key Input value07" },
               { "label": "Custom Label08", "value": "Key Input value08" },
               { "label": "Custom Label09", "value": "Key Input value09" }	
             ]
           },
           { "enabled": False,
             "data": [
               { "label": "Custom Label10", "value": "Key Input value10" },
               { "label": "Custom Label11", "value": "Key Input value11" },
               { "label": "Custom Label12", "value": "Key Input value12" }	
             ]
           },
           { "enabled": True,
             "data": [
               { "label": "Custom Label13", "value": "Key Input value13" },
               { "label": "Custom Label14", "value": "Key Input value14" },
               { "label": "Custom Label15", "value": "Key Input value15" }	
             ]
           }
]


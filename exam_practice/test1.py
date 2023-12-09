import webshop_frontend as wf
# NOTE! this is how to use import!

# oppgave 3.3 - get_all_wares_in_stock Oblig5 - Case 1.
for ware_id, ware in wf.all_wares.items():
    for details in ware.items():
        print(details)

#  ware_id, ware stores the key and value (.items())
#  from the all_wares dictionary.
#  key (which is stored in ware_id) is now: amd_processor, Ps5 etc.
#  value is the dictionary within the key (stored in ware here)
#  which itself has keys and values
#  that are all the details for the ware
#  printing here gives this output:

#  To only get the inner dictionary printed
#  that is all the details for the ware.
#  the inne for loop gets this by:
#  assigning the ware.items() to variable details
#  remember: .items returns a view object (tuple) of
#  key and value for the dict targeted with .items()
#  output is now the following:


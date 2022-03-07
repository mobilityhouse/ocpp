How to start Charge Point Operator and how to connecto Charge Point:

In terminal write:
                    uvicorn cpo-main.v16.CPO.main:app --reload
to start the CPO.
Then you can access fastapi interface from your browser by typing 
                    127.0.0.1:8000/docs
in the search bar.

Once the CPO is operational you can simply run the charge_point.py code to connect the virtual charge point.
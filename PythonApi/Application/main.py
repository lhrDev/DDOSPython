#########################################################################

import uvicorn 

#########################################################################

if __name__ == '__main__':
    uvicorn.run('SoaPythonSecurity:app', 
                host="127.0.0.1",
                port= 8090,
                reload=True
                )
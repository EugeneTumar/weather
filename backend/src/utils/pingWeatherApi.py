from fastapi import FastAPI, HTTPException
import httpx

from ..settings import urls

def ping_api():
    try:
        with httpx.Client() as client:
            response = client.get(urls.api)
            response.raise_for_status() 
            return True
    except HTTPException as e:
        return e.status_code<400
    except Exception as e:
        print(e)
        return False

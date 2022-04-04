c.KernelSpecManager.allowed_kernelspecs = set(['slai_example_venv'])
c.JupyterHub.tornado_settings = {
    "headers": {
        "Content-Security-Policy": "frame-ancestors self http://localhost:3000",
        "Access-Control-Allow-Origin": "http://locahost:3000",
    }
}
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors self http://localhost:3000",
        "Access-Control-Allow-Origin": "http://locahost:3000",        
    }
}
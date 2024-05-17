# AI generate image 


+ ## 1.  Get Started
    - ### register on replicate--> [Replicate](https://replicate.com/)
    - ### copy your api token
    - ### create new package on project --> path:  ``.streamlit/secrets.toml``
    - ### Add your token in ``secrets.toml`` fayil :
        ~~~python
        REPLICATE_API_TOKEN = "your token"
        ~~~

+ ## 2. Runing
    + ### shell
        - ### configurations eviroments:
            ~~~shell
            python -m venv env
            ~~~
            - ### windows
            ~~~shell               
            env\Scripts\activate 
            ~~~
            - ### Linux
            ~~~shell
            source env/bin/actiate
            ~~~
        - ### install modules
            ~~~shell
            pip install -r requirements.txt
            ~~~
        - ### Run
            ~~~shell
            streamlit run main.py
            ~~~
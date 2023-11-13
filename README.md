# lsc 350 infographic
 interactive infographic website for lsc350 describing the global chip shortage

## To run:
clone this repository
### Normal setup:
[install python3](https://www.python.org/downloads/) then do:
0) (recommended) make and activate python env
   1) `python3 -m venv .env`
   2) `source .env/bin/activate`
1) `pip install -r requirements .txt` to install dependancies
2) `streamlit run app.py` to start the app


### Using Docker:
[install docker](https://docs.docker.com/engine/install/) then do:

`docker build . -t lsc_host`\
`docker run -p 8501:8501 -d lsc_host`

or use the `run.sh` script

Open website using going to http://localhost:8501
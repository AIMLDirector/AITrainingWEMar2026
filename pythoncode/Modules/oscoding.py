#in build module - os , sys , time , datetime , random , math , re , json , csv , requests  , time, subprocess , threading , multiprocessing , socket , struct , logging , argparse , configparser 
# external module -- pypi.org -- pandas, numpy , matplotlib , seaborn , scikit-learn , tensorflow , keras , pytorch , xgboost , lightgbm , catboost , statsmodels , scipy , nltk , spacy , gensim , transformers , huggingface  -- for machine learning and data science
# GenAI module -- langchain, openai , cohere , huggingface , transformers , sentence-transformers , textblob , vaderSentiment , wordcloud , pytextrank , sumy , gensim -- for natural language processing and generation
# Agentic Ai module -- crewai, microsoft agent framework, google adk -- for building intelligent agents and chatbots
# Db module -- cx-oracle, pymongo, sqlalchemy , psycopg2 , mysql-connector-python , sqlite3 , redis-py , cassandra-driver , neo4j-driver -- for database connectivity and operations
import osq
from dotenv import load_dotenv   # pip install python-dotenv
load_dotenv()  # Load environment variables from .env file
print(os.getcwd())  # Get current working directory
api_key = os.getenv('OPEN_API_KEY')  # Get API key from environment variable
#print(api_key)  # Print the API key to verify it's loaded correctly
os.environ['Prod_Server'] = "server1" # setting the prod server name

print(os.name)  # Get the name of the operating system

print(os.listdir('/Users/premkumargontrand/AITrainingWEMar2026/'))  # List files and directories in the current directory

if os.path.exists('/Users/premkumargontrand/AITrainingWEMar20277/'):
    print("Path exists")
    
else:
    print("Path does not exist")

os.system("df -h")

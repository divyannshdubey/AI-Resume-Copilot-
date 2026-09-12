from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "mysql+pymysql://f27ZT9Ye5Ns6Ljx.root:@password.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ssl": True
        }
    }
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
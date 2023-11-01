import pynecone as pc

class SnsprojectConfig(pc.Config):
    pass

config = SnsprojectConfig(
    app_name="SNS_project",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
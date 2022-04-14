from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


def cluster():
        cloud_config= {
                'secure_connect_bundle': '<</PATH/TO/>>secure-connect-nigeria-newsapi.zip'
        }
        auth_provider = PlainTextAuthProvider('<<CLIENT ID>>', '<<CLIENT SECRET>>')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        return cluster


def get_session():
        session = cluster.connect()
        return session

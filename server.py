import time
from concurrent import futures
import grpc
import mixer_auth_pb2 as ma
import mixer_auth_pb2_grpc as ma_grpc

SERVER_ADDRESS = '127.0.0.1:1443'  # server address

class MaServicer(ma_grpc.AuthServicer):

    def check(self, req, context):
        print('receive:', str(context.invocation_metadata()))  # print metadata
        rsp = ma.CheckRsp()
        rsp.err_code = 'ok'
        return rsp


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
ma_grpc.add_AuthServicer_to_server(MaServicer(), server)
server.add_insecure_port(SERVER_ADDRESS)
server.start()
while True:
    time.sleep(1)

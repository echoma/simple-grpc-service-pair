import time
import grpc
import mixer_auth_pb2 as ma
import mixer_auth_pb2_grpc as ma_grpc

SERVER_ADDRESS = '127.0.0.1:1443'  # server addresss

while True:  # dead loop
    try:
        # make new connection and send one request
        print(str(time.time()),': connect and send request-----------')
        with grpc.insecure_channel(SERVER_ADDRESS) as channel:
            stub = ma_grpc.AuthStub(channel)
            req = ma.CheckReq()
            rsp = stub.check(req, metadata=(('user_id', '112233'),))  # send request, set metadata
            print(str(time.time()), ': ok')
    except grpc.RpcError as e:
        print(str(time.time()), ': '+str(e))
    finally:
        time.sleep(3)  # loop once every 3 seconds

import logging
import grpc
import proto.rwmanager_pb2 as proto
import proto.rwmanager_pb2_grpc as proto_grpc

from typing import Optional


class RwmsClient:
    def __init__(self, addr: str, port: int):
        options = [("grpc.max_receive_message_length", 300 * 1024 * 1024)]
        self.__channel = grpc.aio.insecure_channel(f"{addr}:{port}", options=options)
        self.__stub = proto_grpc.RwManagerStub(self.__channel)

    async def close(self):
        try:
            await self.__channel.close()

        except grpc.aio.AioRpcError as e:
            logging.error(f"error closing channel: {e}")

    async def add_user(
        self, user: proto.AddUserRequest
    ) -> Optional[proto.UserResponse]:
        try:
            return await self.__stub.AddUser(user)

        except grpc.RpcError as e:
            logging.error(f"error adding user {user.username}: {e}")
            return None

    async def update_user(
        self, user: proto.UpdateUserRequest
    ) -> Optional[proto.UserResponse]:
        try:
            return await self.__stub.UpdateUser(user)

        except grpc.RpcError as e:
            logging.error(f"error updating user {user.uuid}: {e}")
            return None

    async def get_user_by_uuid(self, uuid: str) -> Optional[proto.UserResponse]:
        try:
            return await self.__stub.GetUserByUuid(
                proto.GetUserByUuidRequest(uuid=uuid)
            )

        except grpc.RpcError as e:
            logging.error(f"error getting user by uuid {uuid}: {e}")
            return None

    async def get_user_by_username(self, username: str) -> Optional[proto.UserResponse]:
        try:
            return await self.__stub.GetUserByUsername(
                proto.GetUserByUsernameRequest(username=username)
            )

        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                logging.info(
                    f"user {username} not found (expected for non-existent users)"
                )
                return None

            logging.error(f"error getting user by username {username}: {e}")
            return None

    async def get_all_users(
        self,
        offset: int = None,
        count: int = None,
    ) -> proto.GetAllUsersReply:
        try:
            return await self.__stub.GetAllUsers(
                proto.GetAllUsersRequest(
                    offset=offset,
                    count=count,
                )
            )
        except grpc.RpcError as e:
            logging.error(f"error getting all users: {e}")
            return None

    async def get_inbounds(self) -> Optional[proto.GetInboundsResponse]:
        try:
            return await self.__stub.GetInbounds(proto.Empty())

        except grpc.RpcError as e:
            logging.error(f"error getting inbounds: {e}")
            return None

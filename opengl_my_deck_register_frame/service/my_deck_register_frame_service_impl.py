from opengl_my_deck_register_frame.repository.my_deck_register_frame_repository_impl import MyDeckRegisterFrameRepositoryImpl
from opengl_my_deck_register_frame.service.my_deck_register_frame_service import MyDeckRegisterFrameService
from opengl_my_deck_register_frame.service.request.my_deck_register_request import MyDeckRegisterRequest
from session.service.session_service_impl import SessionServiceImpl


class MyDeckRegisterFrameServiceImpl(MyDeckRegisterFrameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__myDeckRegisterFrameRepository = MyDeckRegisterFrameRepositoryImpl.getInstance()
            cls.__instance.__sessionService = SessionServiceImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    # def createMyDeckRegisterUiFrame(self, rootWindow, switchFrameWithMenuName):
    #
    #     def on_deck_register_click(event, entry_deckname):
    #         try:
    #             session_info = self.__sessionService.getSessionInfo()
    #             if session_info is not None:
    #                 responseData = self.__myDeckRegisterFrameRepository.requestRegister(
    #                     MyDeckRegisterRequest(session_info, entry_deckname.get()))
    #
    #                 print(f"responseData: {responseData}")
    #
    #                 if responseData and responseData.get("is_success") is True:
    #                     switchFrameWithMenuName("my-card-main")
    #                 else:
    #                     print("Invalid or missing response data.")
    #
    #         except Exception as e:
    #             print(f"An error occurred: {e}")
    #
    #     return None

    def on_deck_register_click(self, entry_deckName):
        try:
            session_info = self.__sessionService.getSessionInfo()
            if session_info is not None:
                responseData = self.__myDeckRegisterFrameRepository.requestRegister(
                    MyDeckRegisterRequest(session_info, entry_deckName))

                print(f"responseData: {responseData}")

                if responseData and responseData.get("is_success") is True:
                    #switchFrameWithMenuName("my-card-main")
                    pass
                else:
                    print("Invalid or missing response data.")

        except Exception as e:
            print(f"An error occurred: {e}")


    def injectTransmitIpcChannel(self, transmitIpcChannel):
        print("MyDeckRegisterFrameService: injectTransmitIpcChannel()")
        self.__myDeckRegisterFrameRepository.saveTransmitIpcChannel(transmitIpcChannel)

    def injectReceiveIpcChannel(self, receiveIpcChannel):
        print("MyDeckRegisterFrameService: injectTransmitIpcChannel()")
        self.__myDeckRegisterFrameRepository.saveReceiveIpcChannel(receiveIpcChannel)
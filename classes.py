class Television:
    """
    Class to represent the Television objects.
    """
    MIN_CHANNEL: int = 0     # Minimum TV channel
    MAX_CHANNEL: int = 3     # Maximum TV channel

    MIN_VOLUME: int = 0      # Minimum TV volume
    MAX_VOLUME: int = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Method to set the default state of the TV.
        """
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False

    def power(self):
        """
        Method to turn the TV on/off
        :return: Status of the TV
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self):
        """
        Method to change the channel up
        :return: Channel value
        """
        if self.__status == True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Method to change channel down.
        :return: Channel value
        """
        if self.__status == True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def volume_up(self):
        """
        Method to turn volume up.
        :return: Volume value
        """
        if self.__status == True:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self):
        """
        Method to turn volume down.
        :return: Volume value
        """
        if self.__status == True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self):
        """
        Method to return a string displaying the values of TV status, channel, and volume.
        :return: String of the values of TV status, channel, and volume.
        """
        return f'TV Status: Is On = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

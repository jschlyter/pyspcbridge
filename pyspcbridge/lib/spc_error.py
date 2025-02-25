class SpcError():
    ERROR_MAP = {
        0: "OK",
        1: "OK (limited)",
        10: "ERROR: Probably already isolated or isolated",
        11: "ERROR: Unknown",
        12: "ERROR: Missing ID",
        13: "ERROR: Invalid ID",
        14: "ERROR: Unknown Tag",
        15: "ERROR: Memory Full",
        16: "ERROR: Invalid Data",
        17: "ERROR: Missing Data",
        18: "ERROR: Invalid CRC",
        19: "ERROR: Invalid Length",
        20: "ERROR: Not ready",
        21: "ERROR: Invalid Sequence No",
        22: "ERROR: Invalid Decryption",
        23: "ERROR: Invalid Connection Details",
        24: "ERROR: Invalid Username",
        25: "ERROR: Invalid Password",
        40: "ERROR: Generic check failed",
        50: "ERROR: Active",
        51: "ERROR: Inactive",
        52: "ERROR: Invalid User",
        53: "ERROR: Command only possible in Normal door mode",
        54: "ERROR: Authentication Failed",
        55: "ERROR: Engineer Not Authorized",
        56: "ERROR: Invalid Name",
        57: "ERROR: Invalid Profile",
        58: "ERROR: Invalid Site Code",
        59: "ERROR: Invalid PIN",
        60: "ERROR: Duplicate",
        61: "ERROR: Invalid Card Number",
        62: "ERROR: In use",
        63: "ERROR: Global ID in use",
        64: "ERROR: Global Data Protected",
        65: "ERROR: No Rights",
        66: "ERROR: System Set",
        67: "ERROR: Cannot delete",
        68: "ERROR: Cannot delete last",
        69: "ERROR: Date",
        70: "ERROR: Calendar",
        71: "ERROR: Area",
        72: "ERROR: Door",
        73: "ERROR: Web password not enabled",
        74: "ERROR: Null data",
        75: "ERROR: Bad Command",
        76: "ERROR: Pin Expired",
        77: "ERROR: Command is blocked, probably due to open zones",
        78: "ERROR: Not allowed in Engineer mode",
        79: "ERROR: Cannot delete default profile",
        80: "ERROR: Cannot edit default profile",
        100: "ERROR: XML – Buffer Fail",
        101: "ERROR: XML – Bad Format",
        102: "ERROR: XML – Bad Data",
        103: "ERROR: XML – Unknown Tag",
        104: "ERROR: XML – Compulsory Parameter Not Found",
        120: "ERROR: File – Fail",
        121: "ERROR: File – No Space",
        122: "ERROR: File – Not Found",
        123: "ERROR: File – Header",
        124: "ERROR: File – Flash",
        125: "ERROR: File – Flash Verify",
        126: "ERROR: File – Flash Erase",
        140: "ERROR: HTTP – Compulsory Parameter Not Found",
        160: "ERROR: SAM – WD Output",
        998: "ERROR: Communication error",
        999: "ERROR: Unknown error"
    }

    def __init__(self, code: int) -> None:
        self._code = code
        self._message = self.ERROR_MAP.get(code, "ERROR: Unknowm error")

    @property 
    def message(self) -> str:
        return self._message

    @property 
    def error(self) -> dict:
        return {"code": self._code, "message": self._message}



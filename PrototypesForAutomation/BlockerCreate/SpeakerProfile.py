def speakerType(emails):
    for email in emails:
        speaker_type = email.split("@")[1]
        print(speaker_type)
        position = speaker_type.find("sap.com")
        if position == -1:
            return 'external'
    return 'internal'




from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity

import requests

class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over
        
        if True:
            if "late" in messageProtocolEntity.getBody().lower():
                to="6582688660@s.whatsapp.net"
                message="Hey I'm Suhas's bot, Suhas will be late today"
                receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
                
                outgoingMessageProtocolEntity = TextMessageProtocolEntity(message,to=to)
                    
                self.toLower(receipt)
                self.toLower(outgoingMessageProtocolEntity)
                to="6593872246@s.whatsapp.net"
                message="Sent."
                receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
                
                outgoingMessageProtocolEntity = TextMessageProtocolEntity(message,to=to)
                    
                self.toLower(receipt)
                self.toLower(outgoingMessageProtocolEntity)
            if "test" in messageProtocolEntity.getBody().lower():
                to="6593872246@s.whatsapp.net"
                message="Hi I am online and ready."
                receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
                
                outgoingMessageProtocolEntity = TextMessageProtocolEntity(message,to=to)
                    
                self.toLower(receipt)
                self.toLower(outgoingMessageProtocolEntity)
            if "connection" in messageProtocolEntity.getBody().lower():
                to="6593872246@s.whatsapp.net"
                message="Hi I am online and ready."
                receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
                
                outgoingMessageProtocolEntity = TextMessageProtocolEntity(message,to=to)
                    
                self.toLower(receipt)
                self.toLower(outgoingMessageProtocolEntity)
            if "reboot" in messageProtocolEntity.getBody().lower():
                to="6593872246@s.whatsapp.net"
                message="Commencing reboot."
                receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
                
                outgoingMessageProtocolEntity = TextMessageProtocolEntity(message,to=to)
                    
                self.toLower(receipt)
                self.toLower(outgoingMessageProtocolEntity)
                import os
                os.system('sudo shutdown -r now')
            if "factcheck" in messageProtocolEntity.getBody().lower():
                try:
                    to="6593872246@s.whatsapp.net"

                    url="https://factchecktools.googleapis.com/v1alpha1/claims:search?query="+messageProtocolEntity.getBody().lower().split("+")[1]+"&key=AIzaSyCnJefaZN4-YhmiF1Zcpo4-qH3B5b30Ybk"
                    response=requests.get(url).json()
                    try:
                        message="Claim found: " + response["claims"][0]["text"] +"\n\n\n\n" + "The above claim is " + response["claims"][0]["claimReview"][0]["textualRating"]
                    except:
                        pass
                    receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
                    
                    outgoingMessageProtocolEntity = TextMessageProtocolEntity(message,to=to)
                except:
                    pass
                self.toLower(receipt)
                self.toLower(outgoingMessageProtocolEntity)
            if "spam" in messageProtocolEntity.getBody().lower():
                to="6593872246@s.whatsapp.net"

                email=messageProtocolEntity.getBody().lower().split("+")[1]
                message="Commencing storm"
                outgoingMessageProtocolEntity = TextMessageProtocolEntity(message,to=to)
                    
                self.toLower(receipt)
                self.toLower(outgoingMessageProtocolEntity)
                import os
                os.system("python3 bsd.py " + email)
            
                                
                
                
                
    
    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)

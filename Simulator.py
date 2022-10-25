class Simulator:
    def __init__(self):
        self.isAsTurn=True#轮到谁
        self.isBsTurn=True#轮到谁
        self.time=1#传输时间
        self.round=1#传输轮次

        #A的发送窗口
        self.cwnd=4#大小
        self.wStart=1#起点（包含）
        self.wSend=1#下一个发送
        self.wAck=1#下一个确认
        #B
        self.receive=1
    
        

    def restart(self,ssthresh,rto,a2b,b2a):
        pass
    def send(self,isASuccessful,isBSuccessful):
        pass
    def send_many(self,n):
        pass
    
    def cwnd_history()->list:
        pass
import streamlit as st
from Simulator import Simulator
st.title('TCP拥塞控制演示')
simulator=Simulator()
agree = st.sidebar.radio('',['参数设置','实验运行'])
#---------------------------------------------------------------
if(agree==('参数设置')):
    st.header('简介')
    st.write('''
        此应用用于进行TCP拥塞控制算法的演示，
        用户可以通过点击按钮决定数据包的成功发送或丢失
        并观察cwnd和其他状态参数的变化情况。\n
        我们进行的如下假设以简化问题，
        从而更好的体现算法本身：\n
        1. 接收方B窗口值始终大于cwnd\n
        2. 时间的单位为发送方A发送一个数据报的时间\n
        3. 超时重传时间RTO是固定值
        ''')
    #----------------------------------------------------------------
    st.header('参数设置')
    with st.form("my_form"):
        ssthresh=st.number_input('慢开始门限（ssthresh）：',step=1,min_value=1)
        rto=st.number_input('重传时间（RTO）：',step=1,min_value=1)
        a2b=st.number_input('A → B 时延：',step=1,min_value=1)
        b2a=st.number_input('B → A 时延：',step=1,min_value=1)
        # Every form must have a submit button.
        issubmited=st.form_submit_button("应用参数")
        if(issubmited):
            simulator.restart(ssthresh,rto,a2b,b2a)
    #----------------------------------------------------------------
else:
    st.subheader('当前状态')
    st.write(f"""
        传输轮次：{simulator.round}\n
        时间：{simulator.time}\n
        拥塞窗口cwnd：{simulator.cwnd}\n
        """)
    with st.form("single"):
        a=False
        b=False
        if(simulator.isAsTurn):
            a=st.radio(f"A即将发送报文段 M{simulator.wSend} ,此报文段将：",['成功到达','丢失'])=='成功到达'
        if(simulator.isBsTurn): 
            b=st.radio(f"当前B收到了报文段 M{simulator.receive} ,此报文段将：",['成功到达','丢失'])=='成功到达'
        issubmited=st.form_submit_button("确定")
    
    numMaxSendMany=simulator.cwnd+simulator.wStart-simulator.wSend
    if(numMaxSendMany>1 and simulator.isAsTurn and not simulator.isBsTurn):
        with st.form("multi"):
            rto=st.slider('数量：',step=1,min_value=1,max_value=numMaxSendMany,value=numMaxSendMany)
            issubmited=st.form_submit_button("批量发送报文段并成功确认")
            if(issubmited):
                simulator.send_many(issubmited)

    #----------------------------------------------------------------



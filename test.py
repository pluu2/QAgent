from utils.Utils import dynamic_QM
from utils.QAgent import Q_agent_base
QM = dynamic_QM() 

print(QM.summary())
QM.add_action()

print(QM.summary())

agent=Q_agent_base()
print(agent.table())
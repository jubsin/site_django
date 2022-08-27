from rolepermissions.roles import AbstractUserRole

class professor(AbstractUserRole):
    available_permissions= {'escrever_posts': True, 'escolher_kits':True}
class aluno(AbstractUserRole):
    available_permissions= {'postar_relatorio': True, 'escolher_kits':True}

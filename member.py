class member:
    def __init__(self,p_id,p_name,p_lastname,p_categorie,p_saldo,p_totaalsaldo,p_transacties,p_paydate,p_foto=""):
        self.id = p_id
        self.name = p_name
        self.lastname = p_lastname
        self.categorie = p_categorie
        self.foto = p_foto
        self.saldo = p_saldo
        self.totaalsaldo = p_totaalsaldo
        self.transacties = p_transacties
        self.paydate = p_paydate

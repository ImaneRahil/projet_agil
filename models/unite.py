from openerp import api, exceptions, fields, models


class UniteOeuvre(models.Model):
    _name = 'unite.oeuvre'
  
    unite_oeuvre = fields.Char('Unite Oeuvre', required=True)
    complexite_ids=fields.One2many('unite.complexite','unite_id',string ='Complexite')
    unitee_id = fields.Many2one('project.paramfct', ondelete='cascade', string="parametres projet")
   
class UniteComplexite(models.Model):
    _name = 'unite.complexite'
     
    nom = fields.Char('complexite', required=True)
    coeff_complexite = fields.Float('coef complexite', required=True)
    nb_hr = fields.Float('Nombre Heure', required=True)
    unite_id =fields.Many2one('unite.oeuvre', ondelete='cascade', string="Unite")
    cout_count = fields.Float ('cout', compute='_cout_count')
    @api.one
    def _cout_count(self):
        for record in self:
            record.cout_count = record.coeff_complexite * record.nb_hr


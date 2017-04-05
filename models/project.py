
from openerp import api, exceptions, fields, models

#class ProjectClients(models.Model):
   # _name = 'project.clients'
  #  _inherits = {'res.partner' : 'partner_id'}
    #partner_id=fields.Many2one('res.partner' ondelete='cascade')
    #client=fields.Char('client', required=True)
  

class ProjectParamfct(models.Model):
    _name = 'project.paramfct'

    project_ids = fields.One2many('project.project', 'project_paramfct_id',
                                  'Projects')
    lot = fields.Char('lot', required=True)
    fonctions = fields.Char('fonctions', required=True)
    #project_lots = fields.Many2one('project.lots', 'lots Fonctionels')

class ProjectProfilee(models.Model):
    _name = 'project.profilee'
    
    Ressource = fields.Char('Ressource', required=True)
   
    cout_horaire = fields.Char('cout_horaire', required=True)
    color = fields.Char(
    string="Color",
    help="Choisir une couleur pour le profil"
)
   # project_ids = fields.One2many('project.project', 'profil_id',
                                  #'Projects') 
class ProjectEstimation(models.Model):
    _name = 'project.estimation'
    
    project_ids = fields.One2many('project.project', 'project_est_id',
                                  'Projects')

  
    lot = fields.Char('lot', required=True)
    fonctions = fields.Char('fonctions', required=True)
    unite_oeuvre = fields.Char('unite_oeuvre', required=True)
    nombre = fields.Char('nombre', required=True)
    complexite = fields.Selection([ ('tres simple', 'tres simple'),('simple', 'simple'),('moyen', 'moyen'),('Complex', 'Complex'),],'Complex')
    profil = fields.Char('profil', required=True)
    cout = fields.Integer('cout', required=True)
    #cout_total = fields.Char(compute='_compute_cout_total')
     
class UniteOeuvreee(models.Model):
    _name = 'unite.oeuvreee'
    

    
    unite_oeuvre = fields.Char('unite_oeuvre', required=True)
    complexite = fields.Char('complexite', required=True)
    charge_horaire = fields.Char('charge_horaire', required=True)



#class ProjectLots(models.Model):
    #_name = 'project.lots'

    #libele = fields.Char('libele', required=True)
    #project_paramfct_id = fields.One2many('project.paramfct', 'project_lots_id',
                                 # 'parametres')



class ProjectLot(models.Model):
    _name = 'project.lot'

    libele = fields.Char('libele', required=True)
    image=fields.Binary('image')

class ProjectFonctions(models.Model):
    _name = 'project.fonctions'

    fonction = fields.Char('fonction', required=True)
    
   
 
class ProjectProject(models.Model):
    _inherit = 'project.project'
###########################################################################
    project_paramfct_id = fields.Many2one('project.paramfct', 'Parametres Fonctionels') 
    project_est_id=fields.Many2one('project.estimation', 'Project estimation')
   # project_lots = fields.Many2one('project.lots', 'lots Fonctionels') 
###########################################################################
#class Employee(models.Model):
  #  _name = 'hr.employee'
#   _inherit = 'hr.employee'

 #   children_ids = fields.One2many('my_module', 'employee_id', string="Children")


#class Child(models.Model):
  #  _name = 'my_module'

   # name = fields.Char(required=True, string='Name')

   # birthday = fields.Date(required=True, string='Birthday')

  #  employee_id = fields.Many2one('hr.employee', ondelete='cascade', string="Employee")
########################################################################### 

#@api.depends('name')
#def _compute_cout_total(self):
  #  for rec in self:
    #    rec.cout_total = rec.name.cout_total() if rec.name else False
from openerp import api, exceptions, fields, models

class ProjectFonctions(models.Model):
    _name = 'project.fonctions'

    fonction=fields.Char("fonction",required=True)
    lt_id = fields.Many2one('project.lots', ondelete='cascade', string="lot")
    est_id = fields.Many2one('project.estimation', ondelete='cascade', string="estimation")



class ProjectLots(models.Model):
    _name = 'project.lots'

    #lots_est_id=fields.Many2one('project.estimation', 'Project estimation')
    libele = fields.Char('libele', required=True)
    image=fields.Binary('image')
    fct_ids=fields.One2many('project.fonctions','lt_id',string ='fonctions')

   
    
    #lot_id = fields.Many2one('project.lots',"lot")   		
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
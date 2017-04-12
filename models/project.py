
from openerp import api, exceptions, fields, models

#class ProjectClients(models.Model):
   # _name = 'project.clients'
  #  _inherits = {'res.partner' : 'partner_id'}
    #partner_id=fields.Many2one('res.partner' ondelete='cascade')
    #client=fields.Char('client', required=True)
  

class ProjectParamfct(models.Model):
    _name = 'project.paramfct'

    project_id = fields.Many2one('project.project', 'Projet',
                                    required=True)

    unite_ids=fields.One2many('unite.oeuvre','unitee_id',string ="Unites Oeuvres")
    
    #ct_unite = fields.Float('cout unite ', required=True)




class ProjectProfilee(models.Model):
    _name = 'project.profilee'
    
    Ressource = fields.Char('Ressource', required=True)
   
    cout_horaire = fields.Char('cout_horaire', required=True)
  #  color = fields.Char(
   # string="Color",
    #help="Choisir une couleur pour le profil"
#)
   # project_ids = fields.One2many('project.project', 'profil_id',
                                  #'Projects') 

class ProjectProject(models.Model):
    _inherit = 'project.project'
###########################################################################
    project_paramfct_id = fields.Many2one('project.paramfct', 'Parametres Fonctionels') 
    project_est_id=fields.Many2one('project.estimation', 'Project estimation')

    project_id = fields.One2many('project.paramfct', 'project_id', 'parametre')
   # project_lots = fields.Many2one('project.lots', 'lots Fonctionels') 









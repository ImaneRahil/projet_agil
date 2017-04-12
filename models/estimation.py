from openerp import api, exceptions, fields, models

class ProjectEstimation(models.Model):
    _name = 'project.estimation'
    project_ids = fields.One2many('project.project', 'project_est_id',
                                  'Projects')
    #lots_ids = fields.One2many('project.lots', 'lots_est_id',
                                 # 'lots')
    fct_ids=fields.One2many('project.fonctions','est_id',string ='fonctions')

    lot = fields.Char('lot', required=True)
 
   # unite_oeuvre = fields.Char('unite_oeuvre')
    nombre = fields.Char('nombre')
    #complexite = fields.Selection([ ('tres simple', 'tres simple'),('simple', 'simple'),('moyen', 'moyen'),('Complex', 'Complex'),],'Complex')
    profil = fields.Char('profil')
    cout = fields.Integer('cout')
    #cout_total = fields.Char(compute='_compute_cout_total')
 
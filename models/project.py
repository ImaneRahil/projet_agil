# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models


class UniteOeuvreTemplate(models.Model):
    _name = 'aogp.unite.oeuvre.template'

    name = fields.Char('Unite Oeuvre')
    charge = fields.Float('Charge cout standard')


class ComplexiteTemplate(models.Model):
    _name = 'aogp.complexite.template'

    name = fields.Char('Complexite')
    coef = fields.Float('Coefficient de complexité')


class ProjectProfilTemplate(models.Model):
    _name = 'aogp.project.profil.template'

    name = fields.Char('Profil Ressource ')
    cout_profil = fields.Char('cout horaire')


class UniteOeuvre(models.Model):
    _name = 'aogp.unite.oeuvre'

    project_id = fields.Many2one('project.project', string="Projet")
    uo_template_id = fields.Many2one('aogp.unite.oeuvre.template', string=u"Unité d'oeuvre ")

    @api.multi
    def _get_name(self):
        for obj in self:
            obj.name = '%s [%s]' % (obj.uo_template_id.name, obj.charge_unite)

    name = fields.Char(string='Description', compute='_get_name')

    @api.onchange('uo_template_id')
    def onchange_uo_template_id(self):
        if self.uo_template_id:
            self.charge_unite = self.uo_template_id.charge

    charge_unite = fields.Float('Charge cout standard')
    param_estim_ids = fields.One2many('aogp.project.param.estim', 'unite_oeuvre_id', string='Projet Parametres')


class Complexite(models.Model):
    _name = 'aogp.complexite'

    project_id = fields.Many2one('project.project', string="Projet")
    complexite_template_id = fields.Many2one('aogp.complexite.template', string='Complexité')

    @api.multi
    def _get_name(self):
        for obj in self:
            obj.name = '%s [%s]' % (obj.complexite_template_id.name, obj.coeff_complexite)

    name = fields.Char(string='Description', compute='_get_name')

    @api.onchange('complexite_template_id')
    def onchange_complexite_template_id(self):
        if self.complexite_template_id:
            self.coeff_complexite = self.complexite_template_id.coef

    coeff_complexite = fields.Float('coeff complexite')

    # lier au parametres

    paramm_estim_ids = fields.One2many('aogp.project.param.estim', 'complexite_id', string='Projet Parametres')


class ProjectProfil(models.Model):
    _name = 'aogp.project.profil'

    project_id = fields.Many2one('project.project', 'Projet')
    profil_template_id = fields.Many2one('aogp.project.profil.template', string='Ressource')

    @api.multi
    def _get_name(self):
        for obj in self:
            obj.name = '%s [%s]' % (obj.profil_template_id.name, obj.cout_horaire)

    name = fields.Char(string='Description', compute='_get_name')

    @api.onchange('profil_template_id')
    def onchange_profil_template_id(self):
        if self.profil_template_id:
            self.cout_horaire = self.profil_template_id.cout_profil

    cout_horaire = fields.Char('Cout horaire')

    project_estim_ids = fields.One2many('aogp.project.estimation', 'project_profil_id', string=' Projet Estimation')


class ProjectParamEstim(models.Model):
    _name = 'aogp.project.param.estim'

    def _get_name(self):
        for obj in self:
            obj.name = '%s/ %s [%s]' % (
            obj.unite_oeuvre_id.uo_template_id.name, obj.complexite_id.complexite_template_id.name, obj.charge_std)

    name = fields.Char('Nom', compute=_get_name)
    project_id = fields.Many2one('project.project', 'Projet')
    unite_oeuvre_id = fields.Many2one('aogp.unite.oeuvre', 'Unite oeuvre')
    complexite_id = fields.Many2one('aogp.complexite', 'Complexite')

    def _get_charge(self):
        for obj in self:
            obj.charge_std = obj.unite_oeuvre_id.charge_unite * obj.complexite_id.coeff_complexite

    charge_std = fields.Float('Charge standard', compute=_get_charge)


class ProjectLotTemplate(models.Model):
    _name = 'aogp.project.lot.template'
    name = fields.Char('Lot ')
    # project_fonction_ids = fields.One2many('aogp.project.fonction','lot_tmp_id',string ='Fonctions',  widget="many2many_tags")
    project_fonction_ids = fields.Many2many('aogp.project.fonction', 'lot_template_fonction_rel', 'lot_tmp_id',
                                            'fct_id', string='Fonctions')
    fonction_id = fields.Many2one('aogp.project.fonction', 'Fonction')


class ProjectLot(models.Model):
    _name = 'aogp.project.lot'
    project_id = fields.Many2one('project.project', 'Projet')
    lot_template_id = fields.Many2one('aogp.project.lot.template', string='Lot')

    @api.multi
    def _get_name(self):
        for obj in self:
            obj.name = '%s' % (obj.lot_template_id.name)

    name = fields.Char("Lot", compute='_get_name')

    # project_fonction_ids = fields.One2many('aogp.project.fonction', 'project_fonction_id', string='Fonctions')
    # project_fonction_ids = fields.Many2many('aogp.project.fonction', domain="[('project_fonction_id','=', project_lot_id )]", string='Fonctions',  widget="many2many_tags")

    @api.multi
    def get_fcts(self):
        for obj in self:
            obj._cr.execute(
                "SELECT r.fct_id FROM lot_template_fonction_rel r WHERE r.lot_tmp_id = %s ",
                (obj.lot_template_id.id,))
            obj.computed_fonction_ids = [(6, 0, [row.id for row in self._cr.fetchall()])]

    # @api.multi
    # def _get_domain(self):
    #     for record in self:
    #         record.subject_domain_ids = [(6, 0, [subj.id for subj in record.standard_id.subject_ids])]

    subject_domain_ids = fields.Many2many('subject.subject', string='Subject Domain', compute='_get_domain')
    computed_fonction_ids = fields.Many2many('aogp.project.fonction', 'lot_computed_fonction_rel', 'lot_id', 'fct_id',
                                             compute=get_fcts, string='Fonctions')
    project_fonction_ids = fields.Many2many('aogp.project.fonction', 'lot_fonction_rel', 'lot_id', 'fct_id',
                                            string='Fonctions')

    project_estimm_ids = fields.One2many('aogp.project.estimation', 'project_lot_id', string=' Projet Estimation')


class ProjectFonction(models.Model):
    _name = 'aogp.project.fonction'

    name = fields.Char("Fonction")

    description = fields.Text("Description")

    project_profil_template_id = fields.Many2one('aogp.project.profil.template', ondelete='cascade', string="Profil")

    project_param_estim_template_id = fields.Many2one('aogp.project.param.estim.template', ondelete='cascade',
                                                      string="Objet Estimé")

    charge_related_std = fields.Float(related='project_param_estim_template_id.charge_std')

    nombre = fields.Float('Nombre')

    cout_total = fields.Float(compute='_compute_cout_total')

    @api.one
    def _compute_cout_total(self):
        for record in self:
            record.cout_total = record.charge_related_std * record.nombre

    project_id = fields.Many2one('project.project', 'Projet')
    project_estim_ids = fields.One2many('aogp.project.estimation', 'project_fonction_id', string=' Projet Estimation')

    lot_tmp_id = fields.Many2one('aogp.project.lot.template', 'lot')


# class ProjectFonctionTemplate(models.Model):
#     _name = 'aogp.project.fonction.template'
#     name = fields.Char('Fonction ', required=True)
#     description=fields.Text("Description",required=False)

# project_fonction_template_id = fields.Many2one('aogp.project.lot.template', ondelete='cascade')
class ProjectEstimation(models.Model):
    _name = 'aogp.project.estimation'
    project_id = fields.Many2one('project.project', 'Projet')

    @api.multi
    def _default_lot(self):
        return self.env['aogp.project.lot'].search([])

    project_lot_id = fields.Many2one('aogp.project.lot', string="Lot", widget="many2many_tags")
    # project_lot_id = fields.Many2one('aogp.project.lot', ondelete='cascade', string="Lot", default=lambda self: self.env['aogp.project.lot'].search([]))
    project_fonction_id = fields.Many2one('aogp.project.fonction', ondelete='cascade', string="Fonction")
    project_profil_id = fields.Many2one('aogp.project.profil', ondelete='cascade', string="Profil")
    project_param_estim_id = fields.Many2one('aogp.project.param.estim', ondelete='cascade', string="Objet Estimé")
    charge_related_std = fields.Float(related='project_param_estim_id.charge_std')
    nombre = fields.Float('Nombre')
    cout_total = fields.Float(compute='_compute_cout_total')

    @api.one
    def _compute_cout_total(self):
        for record in self:
            record.cout_total = record.charge_related_std * record.nombre


class ProjectProject(models.Model):
    _inherit = 'project.project'

    @api.multi
    def matrice_complexite_value(self):
        for obj in self:
            list_to_create = []
            for line in obj.param_estim_ids:
                line.unlink()
            if obj.unites_oeuvres_projet_ids and obj.complexite_projet_ids:
                for uo in obj.unites_oeuvres_projet_ids:
                    for comp in obj.complexite_projet_ids:
                        list_to_create.append((0, 0, {'unite_oeuvre_id': uo.id if uo.id else False,
                                                      'complexite_id': comp.id if comp.id else False,
                                                      }))
                obj.write({'param_estim_ids': list_to_create})

        return True

    @api.multi
    def lots_value(self):
        for obj in self:
            list_to_create = []
            for line in obj.project_estim_ids:
                line.unlink()
            if obj.lot_projet_ids:
                for lo in obj.lot_projet_ids:
                    for fct in lo.project_fonction_ids:
                        list_to_create.append((0, 0, {'project_lot_id': lo.id,
                                                      'project_fonction_id': fct.id,
                                                      'project_profil_id': fct.project_profil_template_id.id if fct.project_profil_template_id.id else False,
                                                      # 'project_param_estim_id': fct.project_param_estim_template_id.id if fct.project_param_estim_template_id.id else False,
                                                      'charge_related_std': fct.charge_related_std if fct.charge_related_std else False,
                                                      'nombre': fct.nombre if fct.nombre else False,
                                                      'cout_total': fct.cout_total if fct.cout_total else False,

                                                      }))
                obj.write({'project_estim_ids': list_to_create})
            print
            'list_to_create', list_to_create

        return True
   # @api.multi
    #def lots(self):
     #   for obj in self:
      #      list_to_create = []
       #     for line in obj.lot_projet_ids:
        #        line.unlink()
         #   if obj.lot_projet_ids:
          #      for lo in obj.lot_projet_ids:
           #         for fct in lo.project_fonction_ids:
            #            list_to_create.append((0, 0, {'project_lot_id': lo.id,
             #                                         'project_fonction_id': fct.id,

              #                                        }))
               # obj.write({'project_estim_ids': list_to_create})
            #print
            #'list_to_create', list_to_create
        #return True



    param_estim_ids = fields.One2many('aogp.project.param.estim', 'project_id', string='Parametres Estimation',
                                      ondelete='cascade')
    project_estim_ids = fields.One2many('aogp.project.estimation', 'project_id', string='Estimation',
                                        ondelete='cascade')
    lot_projet_ids = fields.One2many('aogp.project.lot', 'project_id', string='Lots')
    fonctions_projet_ids = fields.One2many('aogp.project.fonction', 'project_id', string='Fonctions')
    profil_projet_ids = fields.One2many('aogp.project.profil', 'project_id', string='Profils', ondelete='cascade')
    complexite_projet_ids = fields.One2many('aogp.complexite', 'project_id', string='Complexités', ondelete='cascade')
    unites_oeuvres_projet_ids = fields.One2many('aogp.unite.oeuvre', 'project_id', string='Unités Oeuvres',
                                                ondelete='cascade')

    @api.multi
    def report_estimation(self, context=None):
        if context is None:
            context = {}
        data = self.read()
        datas = {'model': 'project.project',
                 'form': data,
                 'report_type': 'pdf',
                 }
        return {'type': 'ir.actions.report.xml', 'report_name': 'projet_estimation', 'datas': datas,
                'nodestroy': True, }


class ProjectParamEstimTemplate(models.Model):
    _name = 'aogp.project.param.estim.template'

    def _get_name(self):
        for obj in self:
            obj.name = '%s/ %s [%s]' % (
            obj.unite_oeuvre_template_id.name, obj.complexite_template_id.name, obj.charge_std)

    name = fields.Char('Nom', compute=_get_name)

    unite_oeuvre_template_id = fields.Many2one('aogp.unite.oeuvre.template', 'Unite oeuvre')
    complexite_template_id = fields.Many2one('aogp.complexite.template', 'Complexite')

    def _get_charge(self):
        for obj in self:
            obj.charge_std = obj.unite_oeuvre_template_id.charge * obj.complexite_template_id.coef

    charge_std = fields.Float('Charge standard', compute=_get_charge)


# class ProjectEstimationTemplate(models.Model):
# _name = 'aogp.project.estimation.template'



# project_lot_id = fields.Many2one('aogp.project.lot.template', ondelete='cascade', string="Lot")


# project_fonction_id = fields.Many2one('aogp.project.fonction', ondelete='cascade', string="Fonction", domain="[('project_fonction_id', '=', project_lot_id )]")


# project_profil_template_id = fields.Many2one('aogp.project.profil.template', ondelete='cascade', string="Profil")


# project_param_estim_template_id = fields.Many2one('aogp.project.param.estim.template', ondelete='cascade', string="Objet Estimé")


# charge_related_std = fields.Float(related='project_param_estim_template_id.charge_std')

# nombre = fields.Float('Nombre')

# cout_total = fields.Float(compute='_compute_cout_total')

# @api.one
# def _compute_cout_total(self):
#   for record in self:
#    record.cout_total = record.charge_related_std*record.nombre

# collectivite_ids = fields.Many2many('res.partner', 'calcul_cotisation_collectivite', 'calcul_id', 'partner_id', "Collectivites",
# domain="[('is_collectivite', '=', True), ('contrat_id', '!=', None), ('customer','=',True),('is_company','=',True)]", required=True)

class demo_access_rights(models.Model):
    _name = 'demo.access.rights'
    _rec_name = 'name'
    name = fields.Char('Name')
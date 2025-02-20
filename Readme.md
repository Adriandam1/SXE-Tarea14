# SXE-Tarea14

## Índice  
1. [Enunciado](#1-enunciado)  
2. [Funcionalidad módulo partner_Zodiac](#2-funcionalidad-módulo-partner_zodiac)  
3. [Añadimos los campos a nuestro model](#3-añadimos-los-campos-a-nuestro-model)  
4. [Formulario](#4-formulario)  
5. [Lista](#5-lista)  
6. [Kanban](#6-kanban)  

<br></br>
## 1) Enunciado

Completa la funcionalidad del módulo indicado en la guía de esta semana y además, añade lo siguiente:

- Un campo para almacenar el perfil de LinkedIn del contacto.

- Un campo calculado que determine si el contacto es activo en redes sociales, según si tiene un perfil de LinkedIn registrado o no. Activo si tiene un perfil.
Inactivo si el campo está vacío.

**Modificar las vistas** para incluir los nuevos campos:

**Formulario**: Agregar un apartado "Redes Sociales" con los campos de perfil de LinkedIn y estado de actividad.  
**Lista**: Mostrar el estado de actividad junto al nombre del contacto.  
**Kanban**: Mostrar el enlace de LinkedIn debajo del nombre del contacto.  

Debes entregar un archivo comprimido con el código del módulo de modo que sea instalable. El nombre del módulo debe ser Apellido1Apellido2Nombre

<br></br>
[Volver al inicio](#índice) 

-------------------------------
## 2) Funcionalidad modulo partner_Zodiac:
Añadimos la funcionalidad para aisgnar signo del zodíaco según la fecha

<details><summary>🔍 SPOILER:</summary>  

Nuestro model original de la practica anterior:
  ```bash
from odoo import models, fields, api


class partner_zodiac(models.Model):
     #funciona "como un import"
     _inherit = 'res.partner'
     f_nac = fields.Date("Fecha de nacimiento")
     #NO SE DEBE ALMACENAR LA EDAD EN LA BD, ES MALA PRÁXIS, PERO LO HACEMOS CON FINES DE APRENDIZAJE
     edad = fields.Integer(string="Edad", readOnly = True, compute="_calcular_signo", store= True)
     signo_zodiacal = fields.Char(string="Signo zodiacal", readOnly = True, compute="_calcular_signo", store= True)     
     
     @api.depends('f_nac')
     def _calcular_edad(self):
         for record in self:
             #nos aseguramos que existe la fecha de nacimiento
             if record.f_nac:
                #Inserta aqui el código para calcular la edad
                edad = 130
                record.edad = 130

     @api.depends('f_nac')
     def _calcular_signo(self):
        #Self.ensure_one() se asegura de que se recibe unicamente un registro de ese modo
        #podemos asignarlo unicamente a un registro pero esto puede provocar errores ya que si
        #no nos aseguramos de que unicamente llega un registro, fallará. Para ello podemos usar un try except
            try:
                self.ensure_one()
                #Inserta aqui el código para calcular el signo
                self.signo_zodiacal = "Sin signo"
            except Exception:
                print("Se han pasado varios registros en el datacot a calcular signo")


```
Aquí nuestro view original con su form, list y kanban

```bash
    <record model="ir.ui.view" id="partner_zodiac.form">
      <field name="name">partner_zodiac form</field>
      <field name="model">res.partner</field>
      <field name="inherit_id" ref="base.view_partner_form"/>
      <field name="arch" type="xml">
      <xpath expr="//notebook" position="inside">
        <page string ="Zodiaco">
          <group>
            <field name="f_nac" string="Fecha de nacimiento"/>
            <field name="edad" string="Edad"/>
            <field name="signo_zodiacal" string="Signo del zodiaco"/>
          </group>
        </page>
      </xpath>
      </field>
    </record>

    <record model="ir.ui.view" id="partner_zodiac.list">
      <field name="name">partner_zodiac list</field>
      <field name="model">res.partner</field>
      <field name="inherit_id" ref="base.view_partner_tree"/>
      <field name="arch" type="xml">
        <xpath expr="//tree/field[@name='complete_name']" position="after">
            <field name="signo_zodiacal" string="Signo del zodiaco"/>
        </xpath>
      </field>
    </record>
      
    <record model="ir.ui.view" id="partner_zodiac.kanban">
      <field name="name">partner_zodiac kanban</field>
      <field name="model">res.partner</field>
      <field name="inherit_id" ref="base.res_partner_kanban_view"/>
      <field name="arch" type="xml">
        <xpath expr="//strong[@class='o_kanban_record_title oe_partner_heading']" position="after">
          <br/>  
            <field name="signo_zodiacal"/>
      </xpath>
      </field>
    </record>
```

</details>

<br></br>
[Volver al inicio](#índice) 

## 3) Añadimos los campos a nuestro model:

<details><summary>🔍 SPOILER:</summary>  

Añadimos los nuevos campos *linkedin_profile* y *activo_redes*
```bash
     linkedin_profile = fields.Char(string="Perfil de LinkedIn")
     activo_redes = fields.Selection([('activo', 'Activo'), ('inactivo', 'Inactivo')],
        string="Estado en Redes Sociales",
        compute="_calcular_actividad_redes",
        store=True
    )
```

Modificamos *_calcular_edad* y *_calcular_signo* , añadimos la funcion  *_calcular_actividad_redes*
```bash
     @api.depends('f_nac')
     def _calcular_edad(self):
        from datetime import date
        for record in self:
            if record.f_nac:
                today = date.today()
                record.edad = today.year - record.f_nac.year - ((today.month, today.day) < (record.f_nac.month, record.f_nac.day))

     @api.depends('f_nac')
     def _calcular_signo(self):
        signos = [
            ("Capricornio", (12, 22), (1, 19)),
            ("Acuario", (1, 20), (2, 18)),
            ("Piscis", (2, 19), (3, 20)),
            ("Aries", (3, 21), (4, 19)),
            ("Tauro", (4, 20), (5, 20)),
            ("Géminis", (5, 21), (6, 20)),
            ("Cáncer", (6, 21), (7, 22)),
            ("Leo", (7, 23), (8, 22)),
            ("Virgo", (8, 23), (9, 22)),
            ("Libra", (9, 23), (10, 22)),
            ("Escorpio", (10, 23), (11, 21)),
            ("Sagitario", (11, 22), (12, 21)),
        ]
        for record in self:
            if record.f_nac:
                mes, dia = record.f_nac.month, record.f_nac.day
                for signo, inicio, fin in signos:
                    if (inicio[0] == mes and inicio[1] <= dia) or (fin[0] == mes and fin[1] >= dia):
                        record.signo_zodiacal = signo
                        break

     @api.depends('linkedin_profile')
     def _calcular_actividad_redes(self):
        for record in self:
            record.activo_redes = 'activo' if record.linkedin_profile else 'inactivo'

```

</details>


<br></br>
[Volver al inicio](#índice) 

## 4) Formulario:

```bash
<record model="ir.ui.view" id="partner_zodiac.form">
  <field name="name">partner_zodiac form</field>
  <field name="model">res.partner</field>
  <field name="inherit_id" ref="base.view_partner_form"/>
  <field name="arch" type="xml">
    <xpath expr="//notebook" position="inside">
      <page string="Zodiaco y Redes">
        <group>
          <field name="f_nac" string="Fecha de nacimiento"/>
          <field name="edad" string="Edad"/>
          <field name="signo_zodiacal" string="Signo del zodiaco"/>
          <field name="linkedin_profile" string="Perfil de LinkedIn"/>
          <field name="activo_redes" string="Estado en Redes Sociales"/>
        </group>
      </page>
    </xpath>
  </field>
</record>


```

<br></br>
[Volver al inicio](#índice) 

## 5) Lista:

```bash
<record model="ir.ui.view" id="partner_zodiac.list">
  <field name="name">partner_zodiac list</field>
  <field name="model">res.partner</field>
  <field name="inherit_id" ref="base.view_partner_tree"/>
  <field name="arch" type="xml">
    <xpath expr="//tree/field[@name='complete_name']" position="after">
      <field name="signo_zodiacal" string="Signo"/>
      <field name="linkedin_profile" string="LinkedIn"/>
      <field name="activo_redes" string="Estado"/>
    </xpath>
  </field>
</record>



```

<br></br>
[Volver al inicio](#índice) 

## 6) Kanban: 

```bash
<record model="ir.ui.view" id="partner_zodiac.kanban">
  <field name="name">partner_zodiac kanban</field>
  <field name="model">res.partner</field>
  <field name="inherit_id" ref="base.res_partner_kanban_view"/>
  <field name="arch" type="xml">
    <xpath expr="//strong[@class='o_kanban_record_title oe_partner_heading']" position="after">
      <br/>
      <field name="signo_zodiacal" widget="char" string="Signo"/>
      <field name="linkedin_profile" widget="char" string="LinkedIn"/>
      <field name="activo_redes" widget="statusbar" string="Estado"/>
    </xpath>
  </field>
</record>

```

<br></br>
[Volver al inicio](#índice) 
















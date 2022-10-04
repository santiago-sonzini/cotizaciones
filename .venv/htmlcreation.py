import jinja2 
from htmltopdf import htmltopdf

template = '/Users/santiagosonzini/Desktop/presupuestos/presupuestos/.venv/templates/'

def render_html(template):
    template_loader = jinja2.FileSystemLoader(template)
    template_env = jinja2.Environment(loader=template_loader)
    template_file = "template.html"
    template = template_env.get_template(template_file)
    
    htmltopdf(template.render(
        name=r'Project',
        user_email= 'santisonzini1234@gmail.com',
        servicios = [
            {
     
      "description": "hosting en servers de mycontrol",
      "id": "cl8tjrkar0000vj1fyfljdzvw",
      "name": "Hosting",
      "price": 2332
    },
    {
      "description": "desarrollo de aplicacion web funcional  y lista para comercializacion ",
      "id": "cl8tjtbpo0000wu1fmyzqtz65",
      "name": "Desarrollo web",
      "price": 82342
    },{
      "description": "hosting en servers de mycontrol",
      "id": "cl8tjrkar0000vj1fyfljdzvw",
      "name": "Hosting",
      "price": 2332
    },
    {
      "description": "desarrollo de aplicacion web funcional y lista para comercializacion ",
      "id": "cl8tjtbpo0000wu1fmyzqtz65",
      "name": "Desarrollo web",
      "price": 82342
    }
        ]
        ),'out4.pdf')
            
  
   
    
    
render_html(template)

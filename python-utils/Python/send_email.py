import win32com.client as win32
from datetime import datetime
import os

dia = int(str(datetime.now())[:10].replace('-', ''))

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

mail.Subject = 'Prueba 4 - Sintaxis HMTL + Imagen en local'
mail.to = 'juan.martinez@wom.co'
print(os.getcwd())

attachment = mail.Attachments.Add('C:/Users/jmart/Desktop/Grafico_1.png')
attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "currency_img")

mail.HTMLBody = f'''
<body style="margin: 0;">
    <div>
        <h1>Reporte de Seguimiento {dia} </h1>
            <p>Buenos días, a continuación compartimos el reporte de seguimiento de gross de prepago del día {dia}.</p>
            <h2>1. Calidad del gross</h2>
                <p style="padding-left: 15px;">
                    Para el día 15 de Noviembre del 2022 prepago tuvo un gross de 10.200 usuarios. De esas líneas, el modelo de calidad categoriza el <strong>45% (4590 usuarios)</strong> como usuarios de baja calidad y el <strong>55% (5610)</strong> restante como gross de buena calidad.

                    <br/><br/>

                    A continuación vemos el resumen de los últimos 7 días para ver como la evolución del gross siguiendo estos criterios.
                </p>
                <img 
                    src="https://chartio.com/assets/469a7e/tutorials/charts/stacked-bar-charts/fdf212dcf5089cf3a15082fe16c9bddba8c3a3b8d4bbc196661f0f72f410e260/stacked-bar-misuses-1.png" 
                    alt="Evolución del gross diario según su calidad"
                    style="width: 30%; padding-left: 15px;"
                    >    
                <p style="padding-left: 15px;"> 
                    De igual forma relacionamos a los dealers que trajeron la mayor cantidad de gross de mala calidad para este día:
                </p>
                <img src="cid:currency_img">

            <h2>2. Seguimiento Dealers</h2>
            
                <p style="padding-left: 15px;">
                    Con respecto al comportamiento de los dealers vemos el siguiente panorama: 
                </p>

                <img 
                    src="https://www.analyticslane.com/storage/2018/08/sufijos.png" 
                    alt="Principales KPIs del comportamiento de los dealers"
                    style="width: 30%;padding-left: 15px"
                    >
                
                <p style="padding-left: 15px;">
                    De igual forma nos permitimos adjuntar el reporte completo para que puedan revisar el detalle de cada almacen.
                </p>

            <p>Sin nada más que agregar quedamos atentos a cualquier inquietud.</p>
            <br/><br/>
            <p>Cordial saludo.</p>
    </div>
</body>
'''

mail.Send()
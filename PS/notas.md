Cuando programás un método numérico (ya sea para aproximar derivadas, simular ecuaciones diferenciales o valuar opciones financieras), 
nunca calculás el resultado para un solo valor de h.
Necesitamos realizar un Estudio de Refinamiento de Malla (Grid Refinement Study) para verificar experimentalmente que el código esté bien escrito y que el error decrezca al ritmo teórico previsto por Taylor: $E(h) \approx C h^p$.
Para lograr esto, achicamos $h$ progresivamente (por ejemplo, h in {0.2, 0.1, 0.05,...}) y medimos la velocidad a la que cae el error.

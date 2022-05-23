const personas = [
    { nombre: 'Edu', edad: 35 },
    { nombre: 'Manuel', edad: 37 },
    { nombre: 'Marta', edad: 42 },
    { nombre: 'Edu', edad: 25 },
  ];
  
  const busqueda = personas.reduce((acc, persona) => {
    acc[persona.nombre] = ++acc[persona.nombre] || 0;
    return acc;
  }, {});
  
  console.log(busqueda)

  const duplicados = personas.filter( (persona) => {
      return busqueda[persona.nombre];
  });
  
  console.log(duplicados);
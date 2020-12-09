db.createCollection("packdebienvenida", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required:["name","thematic","price", "quantity","packtype"],
         properties: {
            name: {
               bsonType: "string",
               description: "tu nombre"
            },
	    thematic:{
		bsonType: "string",
		description: "Evento"
	    },
	    price: {
		bsonType: "int",
                description: "Precio del Pack"
	    },
	    quantity:{
		bsonType: "int",
                description: "Cantidad de Packs"
	    },
	    Packtype:{
		bsonType: "string",
                description: "Tipo de pack"
	    },
	    Packlist:{
                    bsonType: "array",
                    items: {
                        bsonType:"object",
                        required: ["name"],
                        properties:{
                            name:{
                                bsonType:"string",
                                description: "Producto del pack"
                            },
                            description:{
                                bsonType:"string",
                                description: "Descripción del elemento"
                            }
                        }
                    }
                
		}}}}})
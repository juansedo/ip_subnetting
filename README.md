# Direccionador IP 🖥💻


## Descripción

Este proyecto hace parte de una motivación personal por el manejo de redes y como aprendizaje del curso de Telemática de la universidad EAFIT en el semestre 2021-1.

Se trata de un programa en Python capaz de crear un esquema de direccionamiento IP a partir de información básica que se explicará más adelante. El método con el que funciona es VLSM (Variable Length Subnet Mask) **(no implementado todavía)**.

Un *input* de ejemplo es el siguiente:
```python
NET_ADDRESS = "212.13.14.0"
NET_MASK = Mask("/24")

LANs = [
  LAN(0, "LAN A", 200),
  LAN(1, "LAN B", 200),
  LAN(2, "LAN C", 200)
]

WANs = [
  (0,1),
  (0,2)
]
```

Un *output* de ejemplo se trata de una tabla con información del esquema IP:
```python
-----------------------------------------------------------
NAME      NETWORK ADDRESS  MASK  BROADCAST        HOSTS
-----------------------------------------------------------
A         212.13.14.0      /27   212.13.14.31     30
A         212.13.14.32     /27   212.13.14.63     30
A         212.13.14.64     /27   212.13.14.95     30
A         212.13.14.96     /27   212.13.14.127    30
A         212.13.14.128    /27   212.13.14.159    30
A         212.13.14.160    /27   212.13.14.191    30
A         212.13.14.192    /27   212.13.14.223    30
A         212.13.14.224    /27   212.13.14.255    30
```

## Autores ✒

- Juan Sebastián Díaz Osorio - *Creador* - [juansedo](https://github.com/juansedo)

## Licencia 📄

Este proyecto está bajo la licencia MIT. Mira el [archivo de licencia](LICENSE.md) para más detalles.
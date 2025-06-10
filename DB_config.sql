use entidade;

CREATE TABLE individuo(
`Id` int auto_increment,
`Specie` varchar(20),
`City` varchar(20),
`Date` date,
`Stable` tinyint(1),
`Injured` tinyint(1),
`Stressed` tinyint(1),
`Observation` varchar(50) not null default '-',
primary key(Id)
);

TRUNCATE TABLE individuo;



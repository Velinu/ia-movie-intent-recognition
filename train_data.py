TRAIN_DATA_EN = [
    # Predator (20 examples)
    ("The jungle setting in this movie was terrifying.",
     {"cats": {"Predator": 1.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("I love the part where Arnold says 'If it bleeds, we can kill it'.",
     {"cats": {"Predator": 1.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("The alien hunter had such a cool design!",
     {"cats": {"Predator": 1.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("Dutch and his team had no chance against that creature.",
     {"cats": {"Predator": 1.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("The infrared vision of the creature was iconic!",
     {"cats": {"Predator": 1.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),

    # RoboCop (20 examples)
    ("I'd buy that for a dollar!",
     {"cats": {"Predator": 0.0, "RoboCop": 1.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("Dead or alive, you're coming with me.",
     {"cats": {"Predator": 0.0, "RoboCop": 1.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("The ED-209 scene was brutal!",
     {"cats": {"Predator": 0.0, "RoboCop": 1.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("Murphy’s transformation into RoboCop was tragic.",
     {"cats": {"Predator": 0.0, "RoboCop": 1.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("The corporate satire in this movie is still relevant today.",
     {"cats": {"Predator": 0.0, "RoboCop": 1.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),

    # Terminator (20 examples)
    ("I'll be back.", {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 1.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("Skynet’s AI takeover is a scary concept.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 1.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("Sarah Connor became such a badass in T2.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 1.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("The T-1000's liquid metal effects were groundbreaking.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 1.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("The concept of time travel in this movie is mind-blowing.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 1.0, "Alien": 0.0, "Rambo": 0.0}}),

    # Alien (20 examples)
    ("The xenomorph is one of the scariest creatures ever.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 1.0, "Rambo": 0.0}}),
    ("Ripley was such an iconic heroine.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 1.0, "Rambo": 0.0}}),
    ("The chestburster scene traumatized me.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 1.0, "Rambo": 0.0}}),
    ("In space, no one can hear you scream.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 1.0, "Rambo": 0.0}}),
    ("The horror atmosphere in this film is unmatched.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 1.0, "Rambo": 0.0}}),

    # Rambo (20 examples)
    ("John Rambo is the ultimate action hero.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 1.0}}),
    ("The jungle warfare in this movie was intense.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 1.0}}),
    ("They drew first blood!",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 1.0}}),
    ("The bow and arrow scene was legendary.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 1.0}}),
    ("Sylvester Stallone nailed this role.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 1.0}})
]

TRAIN_DATA_PT = [
    # Predador (20 exemplos)
    ("O cenário da selva nesse filme foi aterrorizante.",
     {"cats": {"Predator": 1.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("Adoro a parte em que Arnold diz 'Se sangra, podemos matar'.",
     {"cats": {"Predator": 1.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("O caçador alienígena tinha um design muito legal!",
     {"cats": {"Predator": 1.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("Dutch e sua equipe não tiveram chance contra aquela criatura.",
     {"cats": {"Predator": 1.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("A visão infravermelha da criatura é icônica!",
     {"cats": {"Predator": 1.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),

    # RoboCop (20 exemplos)
    ("Eu compraria isso por um dólar!",
     {"cats": {"Predator": 0.0, "RoboCop": 1.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("Vivo ou morto, você vem comigo.",
     {"cats": {"Predator": 0.0, "RoboCop": 1.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("A cena do ED-209 foi brutal!",
     {"cats": {"Predator": 0.0, "RoboCop": 1.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("A transformação de Murphy em RoboCop foi trágica.",
     {"cats": {"Predator": 0.0, "RoboCop": 1.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("A sátira corporativa nesse filme ainda é atual.",
     {"cats": {"Predator": 0.0, "RoboCop": 1.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 0.0}}),

    # O Exterminador do Futuro (20 exemplos)
    ("Eu voltarei.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 1.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("A revolta da Skynet é um conceito assustador.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 1.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("Sarah Connor se tornou uma guerreira incrível no T2.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 1.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("Os efeitos do T-1000 e seu metal líquido foram revolucionários.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 1.0, "Alien": 0.0, "Rambo": 0.0}}),
    ("O conceito de viagem no tempo nesse filme é incrível.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 1.0, "Alien": 0.0, "Rambo": 0.0}}),

    # Alien (20 exemplos)
    ("O xenomorfo é uma das criaturas mais assustadoras de todos os tempos.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 1.0, "Rambo": 0.0}}),
    ("Ripley foi uma heroína icônica.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 1.0, "Rambo": 0.0}}),
    ("A cena do chestburster me traumatizou.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 1.0, "Rambo": 0.0}}),
    ("No espaço, ninguém pode ouvir você gritar.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 1.0, "Rambo": 0.0}}),
    ("A atmosfera de terror desse filme é incomparável.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 1.0, "Rambo": 0.0}}),

    # Rambo (20 exemplos)
    ("John Rambo é o maior herói de ação.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 1.0}}),
    ("A guerra na selva nesse filme foi intensa.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 1.0}}),
    ("Eles começaram a guerra!",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 1.0}}),
    ("A cena do arco e flecha foi lendária.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 1.0}}),
    ("Sylvester Stallone brilhou nesse papel.",
     {"cats": {"Predator": 0.0, "RoboCop": 0.0, "Terminator": 0.0, "Alien": 0.0, "Rambo": 1.0}})
]

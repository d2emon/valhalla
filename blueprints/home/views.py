from flask import render_template
from flask_login import login_required


from . import home


@home.route('/')
def index():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Добро Пожаловать!")


@home.route('/start')
@login_required
def start():
    """
    Render the start template on the /start route
    """
    intro = """
    <p>Огромный пиршественный зал гудел от множества голосов собравшихся.
    Деревянные своды его тонули в сизом дыму, поднимавшемся от многочисленных
    железных жаровен. Посреди дома, окружённый огромными закопченными
    валунами, пылал очаг, дровами для которого служили несколько цельных
    брёвен сосны и дуба. Над этим гигантским костром на медной цепи, каждое
    звено которой простому смертному было бы не по силам даже приподнять с
    земли, висел котёл. Таков был этот котёл, что можно разом сварить в нём
    дюжину дюжин быков, и ещё осталось бы в нём предостаточно места. Дым от
    смолистых поленьев валил столбом, поднимаясь к отверстию в потолке, сквозь
    которое в залу проглядывало мерцающее звёздное небо.</p>
    <p>Вокруг котла стояли накрытые столы, изготовленные из зазубренных и
    покрытых пробоинами боевых щитов; за столами сидели воины. Было их здесь
    дюжина дюжин и ещё трое.</p>
    <p>Лился весёлый эль в рога, покрытые серебряной насечкой; плескал через
    край сладкий мёд в золотых кубках; столы же ломились от всевозможной
    снеди. Дюжина дюжин витязей пировали в зале, но вы не услышали бы смеха,
    не увидели бы улыбок на лицах: лишь о былых сражениях толковали между
    собой собравшиеся воины.</p>
    <p>У очага восседал сам Хозяин Дома. Он был огромного роста, широк в
    плечах, а необъятный живот хозяина поддерживал широкий пояс; в докрасна
    начищенных боках котла отражалась его добродушная физиономия. Неподалёку
    лежала дубина, сработанная из крепкого ясеня в три обхвата, с набитыми по
    всей длине для прочности медными кольцами.</p>
    <p>В очаге варился чёрный кабан, бывший размерами под стать своему
    владельцу. Мяса его с лихвой хватало на прокорм дюжине дюжин воинов, да и
    троим оставалось предостаточно. Каждый из собравшихся знал, что собранные
    после пиршества кости этого волшебного животного вновь поутру оживали, и
    каждый вечер на пиру кабана заново бросали в котёл - таким образом,
    обитавшие в этом доме воители никогда не оставались голодными.</p>
    <p>Три витязя сидели за одним из столов, и поедали мясо чудесного зверя,
    обильно заливая его пивом.</p>
    <p>- Что скажешь, Фаргал? Приготовлено не хуже, чем на императорской кухне
    твоей Карнагрии? - обратился к своему товарищу первый из витязей.</p>
    <p>- Истинно так! - ответил тот, аккуратно счищая засапожным кинжалом мясо
    с кости. Покончив с этим делом, он отложил мосол на специально
    приготовленное блюдо (каждый знает, что кости необходимо оставить в
    целости и сохранности - иначе не удастся вновь оживить Чёрного Кабана).
    - Хотя ты, друг мой Конан, наверняка никогда не пробовал действительно
    изысканной пищи!</p>
    <p>- Не ты один восседал на троне! - обиделся его собеседник. - Я, хоть по
    рождению и киммериец, но не меньше твоего повидал на своём веку. Хаген
    подтвердит мои слова!</p>
    <p>Хаген, Ученик мага, лишь пожал плечами.</p>
    <p>- Мне наскучили ваши вечные споры по всякому поводу. Жду не дождусь
    начала сегодняшнего рассказа. Интересно, кто на сей раз поведает нам о
    своих приключениях?</p>
    <p>Как раз в этот момент Хозяин поднялся со своего места, отставив в
    сторону десятивёдерный чан излюбленной им жирной каши, и грохнул кулаком
    по крышке котла:</p>
    <p>- Эй, воины, собравшиеся в моём Доме! Пришло время для новой саги!</p>
    <p>Присутствовавшие встретили это известие одобрительными возгласами.</p>
    <p>- Как и всегда, нынешней ночью мы будем свидетелями подвигов трёх
    величайших героев, чьи имена прославлены сказителями во все века всех
    населённых миров! Как и всегда, сегодня трое выбранных мной из вашего
    числа развлекут своих товарищей да и меня, старика, повторив один из своих
    бесчисленных подвигов!</p>
    <p>- Да будет так! -вскричали все хором, и древние стены Дома дрогнули от
    их богатырского крика. - Избери же рассказчиков!</p>
    <p>- Я избрал их! - ответил им Хозяин, и его испачканный сажей перст
    указал на троих друзей - Фаргала, варвара и Ученика чародея.</p>
    <p>Дюжина дюжин воинов повернулись к ним, и замерли в ожидании чудесной
    саги.</p>
    <p>По мановению руки Хозяина открылись три двери Дома, от которых в разных
    направлениях расходились три мощёные булыжником дороги.</p>
    <p>- Время вечерних сказаний! -возгласил он. - Кто из вас, величайших из
    воителей, победителей чародеев,  драконов, могучих духов и даже богов,
    первым ступит на свою Дорогу?</p>
    """
    print(intro)
    return render_template(
        'home/start.html',
        title="Добро Пожаловать!",
        intro=intro
    )

from fastapi import APIRouter, Response, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/statuses/200", status_code=200, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>200</H1><H2>OK</H2><H3>Успешно. Запрос успешно обработан.</H3></br>"


@router.put("/statuses/201", status_code=201, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>201</H1><H2>Created</H2><H3>Создано. Запрос успешно выполнен и в результате был создан ресурс. Этот код обычно присылается в ответ на запрос PUT ПОМЕСТИТЬ</H3></br>"


@router.post("/statuses/202", status_code=202, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>202</H1><H2>Accepted</H2><H3>Принято. Запрос принят, но ещё не обработан. Не поддерживаемо, т.е., нет способа с помощью HTTP отправить асинхронный ответ позже, который будет показывать итог обработки запроса. Это предназначено для случаев, когда запрос обрабатывается другим процессом или сервером, либо для пакетной обработки.</H3></br>"


@router.get("/statuses/203", status_code=203, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>203</H1><H2>Non-Authoritative Information</H2><H3>Информация не авторитетна. Этот код ответа означает, что информация, которая возвращена, была предоставлена не от исходного сервера, а из какого-нибудь другого источника. Во всех остальных ситуациях более предпочтителен код ответа 200 OK</H3></br>"


@router.post("/statuses/204", status_code=204, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>204</H1><H2>No Content</H2><H3>Нет содержимого. Нет содержимого для ответа на запрос, но заголовки ответа, которые могут быть полезны, присылаются. Клиент может использовать их для обновления кешированных заголовков полученных ранее для этого ресурса.</H3></br>"


@router.post("/statuses/205", status_code=205, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>205</H1><H2>Reset Content</H2><H3>Сбросить содержимое. Этот код присылается, когда запрос обработан, чтобы сообщить клиенту, что необходимо сбросить отображение документа, который прислал этот запрос.</H3></br>"


@router.get("/statuses/206", status_code=206, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>206</H1><H2>Partial Content</H2><H3>Частичное содержимое. Этот код ответа используется, когда клиент присылает заголовок диапазона, чтобы выполнить загрузку отдельно, в несколько потоков."


@router.get("/statuses/300", status_code=300, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>300</H1><H2>Multiple Choice</H2><H3>Множественный выбор. Этот код ответа присылается, когда запрос имеет более чем один из возможных ответов. И User-agent или пользователь должен выбрать один из ответов. Не существует стандартизированного способа выбора одного из полученных ответов.</H3></br>"


@router.get("/statuses/301", status_code=301, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>301</H1><H2>Moved Permanently</H2><H3>Перемещён на постоянной основе. Этот код ответа значит, что URI запрашиваемого ресурса был изменён. Возможно, новый URI будет предоставлен в ответе.</H3></br>"


@router.get("/statuses/302", status_code=302, response_class=HTMLResponse, tags=["http statuses"])
async def root(request: Request, response: Response):
    response.headers["location"] = str(request.url)
    return "<H1>302</H1><H2>Found</H2><H3>Найдено. Этот код ответа значит, что запрошенный ресурс временно изменён. Новые изменения в URI могут быть доступны в будущем. Таким образом, этот URI, должен быть использован клиентом в будущих запросах.</H3></br>"


@router.get("/statuses/303", status_code=303, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>303</H1><H2>See Other</H2><H3>Просмотр других ресурсов. Этот код ответа присылается, чтобы направлять клиента для получения запрашиваемого ресурса в другой URI с запросом GET.</H3></br>"


@router.get("/statuses/304", status_code=304, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>304</H1><H2>Not Modified</H2><H3>Не модифицировано. Используется для кеширования. Это код ответа значит, что запрошенный ресурс не был изменён. Таким образом, клиент может продолжать использовать кешированную версию ответа.</H3></br>"


@router.get("/statuses/305", status_code=305, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>305</H1><H2>Use Proxy</H2><H3>Использовать прокси. Это означает, что запрошенный ресурс должен быть доступен через прокси. Этот код ответа в основном не поддерживается из соображений безопасности.</H3></br>"


@router.get("/statuses/306", status_code=306, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>306</H1><H2>Switch Proxy</H2><H3>Больше не использовать. Изначально подразумевалось, что  последующие запросы должны использовать указанный прокси.</H3></br>"


@router.get("/statuses/307", status_code=307, response_class=HTMLResponse, tags=["http statuses"])
async def root(request: Request, response: Response):
    response.headers["location"] = str(request.url)
    return "<H1>307</H1><H2>Temporary Redirect</H2><H3>Временное перенаправление. Сервер отправил этот ответ, чтобы клиент получил запрошенный ресурс на другой URL-адрес с тем же методом, который использовал предыдущий запрос. Данный код имеет ту же семантику, что код ответа 302 Found, за исключением того, что агент пользователя не должен изменять используемый метод HTTP: если в первом запросе использовался POST, то во втором запросе также должен использоваться POST.</H3></br>"


@router.get("/statuses/308", status_code=308, response_class=HTMLResponse, tags=["http statuses"])
async def root(request: Request, response: Response):
    response.headers["location"] = str(request.url)
    return "<H1>308</H1><H2>Permanent Redirect</H2><H3>Перенаправление на постоянной основе. Это означает, что ресурс теперь постоянно находится в другом URI, указанном в заголовке Location: HTTP Response. Данный код ответа имеет ту же семантику, что и код ответа 301 Moved Permanently, за исключением того, что агент пользователя не должен изменять используемый метод HTTP: если POST использовался в первом запросе, POST должен использоваться и во втором запросе.</H3></br>"


@router.get("/statuses/400", status_code=400, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>400</H1><H2>Bad Request</H2><H3>Плохой запрос. Этот ответ означает, что сервер не понимает запрос из-за неверного синтаксиса.</H3></br>"


@router.get("/statuses/401", status_code=401, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>401</H1><H2>Unauthorized</H2><H3>Неавторизованно. Для получения запрашиваемого ответа нужна аутентификация. Статус похож на статус 403, но,в этом случае, аутентификация возможна.</H3></br>"


@router.get("/statuses/402", status_code=402, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>402</H1><H2>Payment Required</H2><H3>Необходима оплата. Этот код ответа зарезервирован для будущего использования. Первоначальная цель для создания этого кода была в использовании его для цифровых платёжных систем(на данный момент не используется).</H3></br>"


@router.get("/statuses/403", status_code=403, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>403</H1><H2>Forbidden</H2><H3>Запрещено. У клиента нет прав доступа к содержимому, поэтому сервер отказывается дать надлежащий ответ.</H3></br>"


@router.get("/statuses/404", status_code=404, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>404</H1><H2>Not Found</H2><H3>Не найден. Сервер не может найти запрашиваемый ресурс. Код этого ответа, наверно, самый известный из-за частоты его появления в вебе.</H3></br>"


@router.get("/statuses/405", status_code=405, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>405</H1><H2>Method Not Allowed</H2><H3>Метод не разрешён. Сервер знает о запрашиваемом методе, но он был деактивирован и не может быть использован. Два обязательных метода, GET и HEAD, никогда не должны быть деактивированы и не должны возвращать этот код ошибки.</H3></br>"


@router.post("/statuses/406", status_code=406, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>406</H1><H2>Not Acceptable</H2><H3>Этот ответ отсылается, когда веб сервер после выполнения server-driven content negotiation, не нашёл контента, отвечающего критериям, полученным из user agent.</H3></br>"


@router.get("/statuses/407", status_code=407, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>407</H1><H2>Proxy Authentication Required</H2><H3>Этот код ответа аналогичен коду 401, только аутентификация требуется для прокси сервера.</H3></br>"


@router.get("/statuses/408", status_code=408, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>408</H1><H2>Request Timeout</H2><H3>Ответ с таким кодом может прийти, даже без предшествующего запроса. Он означает, что сервер хотел бы отключить это неиспользуемое соединение. Этот метод используется все чаще с тех пор, как некоторые браузеры, вроде Chrome и IE9, стали использовать HTTP механизмы предварительного соединения для ускорения сёрфинга (смотрите баг 634278, будущей реализации этого механизма в Firefox). Также учитывайте, что некоторые серверы прерывают соединения не отправляя подобных сообщений.</H3></br>"


@router.get("/statuses/409", status_code=409, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>409</H1><H2>Conflict</H2><H3>Этот ответ отсылается, когда запрос конфликтует с текущим состоянием сервера.</H3></br>"


@router.get("/statuses/410", status_code=410, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>410</H1><H2>Gone</H2><H3>Этот ответ отсылается, когда запрашиваемый контент удалён с сервера.</H3></br>"


@router.get("/statuses/411", status_code=411, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>411</H1><H2>Length Required</H2><H3>Запрос отклонён, потому что сервер требует указание заголовка Content-Length, но он не указан.</H3></br>"


@router.post("/statuses/412", status_code=412, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>412</H1><H2>Precondition Failed</H2><H3>Клиент указал в своих заголовках условия, которые сервер не может выполнить</H3></br>"


@router.post("/statuses/413", status_code=413, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>413</H1><H2>Request Entity Too Large</H2><H3>Размер запроса превышает лимит, объявленный сервером. Сервер может закрыть соединение, вернув заголовок Retry-After</H3></br>"


@router.get("/statuses/414", status_code=414, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>414</H1><H2>Request-URI Too Long</H2><H3>URI запрашиваемый клиентом слишком длинный для того, чтобы сервер смог его обработать</H3></br>"


@router.post("/statuses/415", status_code=415, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>415</H1><H2>Unsupported Media Type</H2><H3>Медиа формат запрашиваемых данных не поддерживается сервером, поэтому запрос отклонён</H3></br>"


@router.post("/statuses/416", status_code=416, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>416</H1><H2>Requested Range Not Satisfiable</H2><H3>Диапазон указанный заголовком запроса Range не может быть выполнен; возможно, он выходит за пределы переданного URI</H3></br>"


@router.get("/statuses/417", status_code=417, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>417</H1><H2>Expectation Failed</H2><H3>Этот код ответа означает, что ожидание, полученное из заголовка запроса Expect, не может быть выполнено сервером.</H3></br>"


@router.get("/statuses/422", status_code=422, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>422</H1><H2>Unprocessable entity</H2><H3>Код состояния ответа HTTP 422 Unprocessable Entity указывает, что сервер понимает тип содержимого в теле запроса и синтаксис запроса является правильным, но серверу не удалось обработать инструкции содержимого.</H3></br>"


@router.get("/statuses/500", status_code=500, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>500</H1><H2>Internal Server Error</H2><H3>Внутренняя ошибка сервера. Сервер столкнулся с ситуацией, которую он не знает как обработать.</H3></br>"


@router.get("/statuses/501", status_code=501, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>501</H1><H2>Not Implemented</H2><H3>Не реализовано. Метод запроса не поддерживается сервером и не может быть обработан. Единственные методы, которые сервера должны поддерживать (и, соответственно, не должны возвращать этот код) - GET и HEAD.</H3></br>"


@router.get("/statuses/502", status_code=502, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>502</H1><H2>Bad Gateway</H2><H3>Плохой шлюз. Эта ошибка означает что сервер, во время работы в качестве шлюза для получения ответа, нужного для обработки запроса, получил недействительный (недопустимый) ответ.</H3></br>"


@router.get("/statuses/503", status_code=503, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>503</H1><H2>Service Unavailable</H2><H3>Сервис недоступен. Сервер не готов обрабатывать запрос. Зачастую причинами являются отключение сервера или то, что он перегружен. Обратите внимание, что вместе с этим ответом удобная для пользователей(user-friendly) страница должна отправлять объяснение проблемы. Этот ответ должен использоваться для временных условий и Retry-After: HTTP-заголовок должен, если возможно, содержать предполагаемое время до восстановления сервиса. Веб-мастер также должен позаботиться о заголовках, связанных с кешем, которые отправляются вместе с этим ответом, так как эти ответы, связанные с временными условиями, обычно не должны кешироваться.</H3></br>"


@router.get("/statuses/504", status_code=504, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>504</H1><H2>Gateway Timeout</H2><H3>Этот ответ об ошибке предоставляется, когда сервер действует как шлюз и не может получить ответ вовремя.</H3></br>"


@router.get("/statuses/505", status_code=505, response_class=HTMLResponse, tags=["http statuses"])
async def root():
    return "<H1>505</H1><H2>HTTP Version Not Supported</H2><H3>HTTP-версия не поддерживается. HTTP-версия, используемая в запросе, не поддерживается сервером.</H3></br>"

class ViewHelp:
    @staticmethod
    def help(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "Существующие команды:\n\n"
            "* /global_stats - отображает глобальную статистику рынка\n"
            "* /top_coins {Кол-во криптовалют} - выводит заданное кол-во топ криптовалют\n"
            "* /crypto_stats {Slug крипты} - вывод основной статистики криптовалюты\n"
            "* /stacking_info {ISO крипты} - информация о стейкинге криптовалюты\n"
            "* /fear_and_greed_data {Кол-во дней для визуализации} - отображает изменение индекса страха и жадности за выбранный период\n"
            "* /ohlc {Slug крипты} {Кол-во дней для визуализации} - визуализация японских свечей криптовалюты\n"
            "* /market_chart {Slug крипты} {Кол-во дней для визуализации} - визуализация тренда криптовалюты\n"           
                        
            "* /create_asset_portfolio - создание/обнуление портфеля активов\n"
            "* /change_asset {Slug крипты} {Кол-во криптовалюты} - задать или изменить данные об активе в портфеле\n"
            "* /delet_asset {Slug крипты} - удалить актив из портфеля\n"
            "* /get_assets - получение всех активов вашего портфеля\n"
            "* /visualise_asset_portfolio - визуализация активов\n"
            "* /assets_portfolio_changes - изменение цены портфеля от времени\n"
            
            "\nБолее подробную информацию о командах можно посмотреть написав её после /help, например: "
            "/help /top_coins или /help top_coins"
        )

    @staticmethod
    def menu_help(call, **kwargs):
        kwargs["bot"].answer_callback_query(call.id, "Помощь выведена")
        kwargs["bot"].send_message(
            call.from_user.id,
            "Существующие команды:\n\n"
            "* /global_stats - отображает глобальную статистику рынка\n"
            "* /top_coins {Кол-во криптовалют} - выводит заданное кол-во топ криптовалют\n"
            "* /crypto_stats {Slug крипты} - вывод основной статистики криптовалюты\n"
            "* /stacking_info {ISO крипты} - информация о стейкинге криптовалюты\n"
            "* /fear_and_greed_data {Кол-во дней для визуализации} - отображает изменение индекса страха и жадности за выбранный период\n"
            "* /ohlc {Slug крипты} {Кол-во дней для визуализации} - визуализация японских свечей криптовалюты\n"
            "* /market_chart {Slug крипты} {Кол-во дней для визуализации} - визуализация тренда криптовалюты\n"

            "* /create_asset_portfolio - создание/обнуление портфеля активов\n"
            "* /change_asset {Slug крипты} {Кол-во криптовалюты} - задать или изменить данные об активе в портфеле\n"
            "* /delet_asset {Slug крипты} - удалить актив из портфеля\n"
            "* /get_assets - получение всех активов вашего портфеля\n"
            "* /visualise_asset_portfolio - визуализация активов\n"
            "* /assets_portfolio_changes - изменение цены портфеля от времени\n"

            "\nБолее подробную информацию о командах можно посмотреть написав её после /help, например: "
            "/help /top_coins или /help top_coins"
        )

    @staticmethod
    def help_global_stats(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "Данная команда позволяет отследить текущее состояние рынка. "
            "Доминацию основных монет, капитадизацию и циркуляцию денег в рынке. "
            "Так-же команда позволяет отследить текущий индекс страха и жадности."
        )

    @staticmethod
    def help_top_coins(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "Данная команда позволяет вывести информацию о топ криптовалютах. "
            "Как доп аргумент туда можно передать кол-во топ монет, которое вы хотите увидеть. "
            "Если в функцию ничего не передавать, то выведется топ 20 криптовалют.\n\n"
            "Аргументы: {Кол-во криптовалют} - целое число, отвечающее за вывод кол-ва топ криптовалют.\n"
            "(На данный момент максимальное кол-во криптовалют для просмотра: 150)"
        )

    @staticmethod
    def help_crypto_stats(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "Данная команда позволяет вывести основную информацию о криптовалюте: "
            "Дату создания, ценность криптовалюты, её особенности, а так-же динамику цены.\n\n"
            "Аргументы: {Slug крипты} - название криптовалюты, которое используется CoinGecko "
            "в разделе 'Идентификатор API'."
        )

    @staticmethod
    def help_stacking_info(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "Данная команда позволяет получить основную информацию о стейкинге той или иной криптовалюты. "
            "Для того, чтобы стейкать криптовалюту - она должна использовать алгоритм PoS или её вариацию.\n\n"
            "Аргументы: {ISO крипты} - аббревиатура криптовалюты, которую можно найти на CoinGecko или CoinMarketCap.\n"
            "(Данные берутся из Staking Rewards)"
        )

    @staticmethod
    def help_fear_and_greed_data(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "Данная команда позволяет получить основную информацию об изменении индекса страха и жадности "
            "с течением времени.\n\n"
            "Аргументы: {Кол-во дней для визуализации} - кол-во дней с которых мы хотим получить информацию. "
            "Визуализация заканчивается текущим днём.\n"
        )

    @staticmethod
    def help_ohlc(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "Данная команда создаёт визуализацию японских свечей выбранной криптовалюты от usd.\n\n"
            "Аргументы: {Slug крипты} - название криптовалюты, которое используется CoinGecko "
            "в разделе 'Идентификатор API', {Кол-во дней для визуализации} - кол-во дней с которых мы хотим получить "
            "информацию.\n"
            "(Возможное кол-во дней: 1/7/14/30/90/180/365/max)"
        )

    @staticmethod
    def help_market_chart(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "Данная команда создаёт визуализацию тренда цены выбранной криптовалюты от usd.\n\n"
            "Аргументы: {Slug крипты} - название криптовалюты, которое используется CoinGecko "
            "в разделе 'Идентификатор API', {Кол-во дней для визуализации} - кол-во дней с которых мы хотим получить "
            "информацию.\n"
            "(Любое кол-во дней, включая max)"
        )

    @staticmethod
    def help_create_asset_portfolio(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "С помощью этой команды можно создать портфель активов. Если портфель существует, то он обнулится."
            "Без созданного портфеля нельзя производить команды с ним."
        )

    @staticmethod
    def help_change_asset(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "С помощью этой команды можно задать криптовалюту и её кол-во в портфеле. "
            "Если выбранная криптовалюта уже есть, то её цена будет изменена.\n\n"
            "Аргументы: {Slug крипты} - название криптовалюты, которое используется CoinGecko "
            "в разделе 'Идентификатор API', {Кол-во криптовалюты} - кол-во криптовалюты, которое вы хотите внести или "
            "изменить в своём портфеле."
        )

    @staticmethod
    def help_delete_asset(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "С помощью этой команды можно удалить актив из портфеля.\n\n"
            "Аргументы: {Slug крипты} - название криптовалюты, которое используется CoinGecko "
            "в разделе 'Идентификатор API'."
        )

    @staticmethod
    def help_get_assets(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "С помощью этой команды можно получить все криптовалюты, которые есть на данный момент в вашем портфеле."
        )

    @staticmethod
    def help_visualise_asset_portfolio(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "С помощью этой команды можно в удобном формате увидеть соотношение криптовалют в портфеле и "
            "отследить его текущую цену."
        )

    @staticmethod
    def help_assets_portfolio_changes(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "С помощью этой команды можно в удобном формате отследить изменение цены криптовалюты "
            "вашего портфеля в зависимости от времени."
        )

    @staticmethod
    def no_command(message, **kwargs):
        kwargs["bot"].send_message(
            message.chat.id,
            "Такой команды не существует...."
        )



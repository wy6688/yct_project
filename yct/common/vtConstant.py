# encoding: UTF-8

# 默认空值
EMPTY_STRING = ''
EMPTY_UNICODE = u''
EMPTY_INT = 0
EMPTY_FLOAT = 0.0

# 方向常量
DIRECTION_NONE = u'none'
DIRECTION_LONG = u'long'
DIRECTION_SHORT = u'short'
DIRECTION_UNKNOWN = u'unknown'
DIRECTION_NET = u'net'
DIRECTION_SELL = u'sell'      # IB接口
DIRECTION_COVEREDSHORT = u'covered short'    # 证券期权

# 开平常量
OFFSET_NONE = u'none'
OFFSET_OPEN = u'open'
OFFSET_CLOSE = u'close'
OFFSET_CLOSETODAY = u'close today'
OFFSET_CLOSEYESTERDAY = u'close yesterday'
OFFSET_UNKNOWN = u'unknown'

# 状态常量
STATUS_NOTTRADED = u'pending'
STATUS_PARTTRADED = u'partial filled'
STATUS_ALLTRADED = u'filled'
STATUS_CANCELLED = u'cancelled'
STATUS_REJECTED = u'rejected'
STATUS_UNKNOWN = u'unknown'

# 合约类型常量
PRODUCT_EQUITY = u'equity'
PRODUCT_FUTURES = u'futures'
PRODUCT_OPTION = u'option'
PRODUCT_INDEX = u'index'
PRODUCT_COMBINATION = u'combination'
PRODUCT_FOREX = u'forex'
PRODUCT_UNKNOWN = u'unknown'
PRODUCT_SPOT = u'spot'
PRODUCT_DEFER = u'defer'
PRODUCT_NONE = 'none'

# 价格类型常量
PRICETYPE_LIMITPRICE = u'limit order'
PRICETYPE_MARKETPRICE = u'market order'
PRICETYPE_FAK = u'FAK'
PRICETYPE_FOK = u'FOK'

# 期权类型
OPTION_CALL = u'call'
OPTION_PUT = u'put'

# 交易所类型
EXCHANGE_SSE = 'SSE'       # 上交所
EXCHANGE_SZSE = 'SZSE'     # 深交所
EXCHANGE_CFFEX = 'CFFEX'   # 中金所
EXCHANGE_SHFE = 'SHFE'     # 上期所
EXCHANGE_CZCE = 'CZCE'     # 郑商所
EXCHANGE_DCE = 'DCE'       # 大商所
EXCHANGE_SGE = 'SGE'       # 上金所
EXCHANGE_INE = 'INE'       # 国际能源交易中心
EXCHANGE_UNKNOWN = 'UNKNOWN'# 未知交易所
EXCHANGE_NONE = ''          # 空交易所
EXCHANGE_HKEX = 'HKEX'      # 港交所
EXCHANGE_HKFE = 'HKFE'      # 香港期货交易所

EXCHANGE_SMART = 'SMART'       # IB智能路由（股票、期权）
EXCHANGE_NYMEX = 'NYMEX'       # IB 期货
EXCHANGE_GLOBEX = 'GLOBEX'     # CME电子交易平台
EXCHANGE_IDEALPRO = 'IDEALPRO' # IB外汇ECN

EXCHANGE_CME = 'CME'           # CME交易所
EXCHANGE_ICE = 'ICE'           # ICE交易所
EXCHANGE_LME = 'LME'           # LME交易所

EXCHANGE_OANDA = 'OANDA'       # OANDA外汇做市商
EXCHANGE_FXCM = 'FXCM'         # FXCM外汇做市商

EXCHANGE_OKCOIN = 'OKCOIN'       # OKCOIN比特币交易所
EXCHANGE_HUOBI = 'HUOBI'         # 火币比特币交易所
EXCHANGE_LBANK = 'LBANK'         # LBANK比特币交易所
EXCHANGE_KORBIT = 'KORBIT'	 # KORBIT韩国交易所
EXCHANGE_ZB = 'ZB'		 # 比特币中国比特币交易所
EXCHANGE_OKEX = 'OKEX'		 # OKEX比特币交易所
EXCHANGE_ZAIF = "ZAIF"		 # ZAIF日本比特币交易所
EXCHANGE_COINCHECK = "COINCHECK" # COINCHECK日本比特币交易所

# 货币类型
CURRENCY_USD = 'USD'            # 美元
CURRENCY_CNY = 'CNY'            # 人民币
CURRENCY_HKD = 'HKD'            # 港币
CURRENCY_UNKNOWN = 'UNKNOWN'    # 未知货币
CURRENCY_NONE = ''              # 空货币

# 数据库
LOG_DB_NAME = 'VnTrader_Log_Db'

# 接口类型
GATEWAYTYPE_EQUITY = 'equity'                   # 股票、ETF、债券
GATEWAYTYPE_FUTURES = 'futures'                 # 期货、期权、贵金属
GATEWAYTYPE_INTERNATIONAL = 'international'     # 外盘
GATEWAYTYPE_BTC = 'btc'                         # 比特币
GATEWAYTYPE_DATA = 'data'                       # 数据（非交易）


# 数据库名称
LOG_DB_NAME = 'VnTrader_Log_Db'
SETTING_DB_NAME = 'VnTrader_Setting_Db'
POSITION_DB_NAME = 'VnTrader_Position_Db'

TICK_DB_NAME = 'VnTrader_Tick_Db'
MINUTE_DB_NAME = 'VnTrader_1Min_Db'
MINUTE_5_DB_NAME = 'VnTrader_5Min_Db'
MINUTE_15_DB_NAME = 'VnTrader_15Min_Db'
MINUTE_30_DB_NAME = 'VnTrader_30Min_Db'
MINUTE_60_DB_NAME = 'VnTrader_60Min_Db'
DAILY_DB_NAME = 'VnTrader_Daily_Db'
WEEKLY_DB_NAME = 'VnTrader_Weekly_Db'

CHT_NODE_5_DB_NAME = 'VnTrader_ChtNode_5Min_Db'
CHT_NODE_30_DB_NAME = 'VnTrader_ChtNode_30Min_Db'
CHT_NODE_D_DB_NAME = 'VnTrader_ChtNode_Daily_Db'
CHT_CB_5_DB_NAME = 'VnTrader_ChtCb_5Min_Db'
CHT_CB_30_DB_NAME = 'VnTrader_ChtCb_30Min_Db'
CHT_CB_D_DB_NAME = 'VnTrader_ChtCb_Daily_Db'


DB_NAME_DICT = {
'1MIN': MINUTE_DB_NAME,
'5MIN':MINUTE_5_DB_NAME,
'15MIN':MINUTE_15_DB_NAME,
'30MIN':MINUTE_30_DB_NAME,
'60MIN':MINUTE_60_DB_NAME,
'D':DAILY_DB_NAME,
'W':WEEKLY_DB_NAME
}

DATABASE_NAMES = [MINUTE_DB_NAME, MINUTE_5_DB_NAME, MINUTE_15_DB_NAME, MINUTE_30_DB_NAME, MINUTE_60_DB_NAME, DAILY_DB_NAME, WEEKLY_DB_NAME,CHT_NODE_5_DB_NAME , \
                  CHT_NODE_30_DB_NAME,CHT_NODE_D_DB_NAME,CHT_CB_5_DB_NAME,CHT_CB_30_DB_NAME,CHT_CB_D_DB_NAME]

# 行情记录模块事件
EVENT_DATARECORDER_LOG = 'eDataRecorderLog'     # 行情记录日志更新事件


EVENT_BAR_5 = 'bar_5min'
import datetime

from sqlalchemy import Column, Float, Integer
from sqlalchemy.dialects.sqlite import DATETIME

from database import Base


class SET50Base():
    ADVANC = Column(Float)
    AOT = Column(Float)
    AWC = Column(Float)
    BANPU = Column(Float)
    BBL = Column(Float)
    BDMS = Column(Float)
    BEM = Column(Float)
    BGRIM = Column(Float)
    BH = Column(Float)
    BTS = Column(Float)
    CBG = Column(Float)
    CENTEL = Column(Float)
    COM7 = Column(Float)
    CPALL = Column(Float)
    CPF = Column(Float)
    CPN = Column(Float)
    CRC = Column(Float)
    DELTA = Column(Float)
    EA = Column(Float)
    EGCO = Column(Float)
    GLOBAL = Column(Float)
    GPSC = Column(Float)
    GULF = Column(Float)
    HMPRO = Column(Float)
    INTUCH = Column(Float)
    IVL = Column(Float)
    KBANK = Column(Float)
    KCE = Column(Float)
    KTB = Column(Float)
    KTC = Column(Float)
    LH = Column(Float)
    MINT = Column(Float)
    MTC = Column(Float)
    OR = Column(Float)
    OSP = Column(Float)
    PTT = Column(Float)
    PTTEP = Column(Float)
    PTTGC = Column(Float)
    RATCH = Column(Float)
    SAWAD = Column(Float)
    SCB = Column(Float)
    SCC = Column(Float)
    SCGP = Column(Float)
    TISCO = Column(Float)
    TLI = Column(Float)
    TOP = Column(Float)
    TRUE = Column(Float)
    TTB = Column(Float)
    TU = Column(Float)
    WHA = Column(Float)


class BacktestBase():
    ADVANC_test = Column(Float)
    AOT_test = Column(Float)
    AWC_test = Column(Float)
    BANPU_test = Column(Float)
    BBL_test = Column(Float)
    BDMS_test = Column(Float)
    BEM_test = Column(Float)
    BGRIM_test = Column(Float)
    BH_test = Column(Float)
    BTS_test = Column(Float)
    CBG_test = Column(Float)
    CENTEL_test = Column(Float)
    COM7_test = Column(Float)
    CPALL_test = Column(Float)
    CPF_test = Column(Float)
    CPN_test = Column(Float)
    CRC_test = Column(Float)
    DELTA_test = Column(Float)
    EA_test = Column(Float)
    EGCO_test = Column(Float)
    GLOBAL_test = Column(Float)
    GPSC_test = Column(Float)
    GULF_test = Column(Float)
    HMPRO_test = Column(Float)
    INTUCH_test = Column(Float)
    IVL_test = Column(Float)
    KBANK_test = Column(Float)
    KCE_test = Column(Float)
    KTB_test = Column(Float)
    KTC_test = Column(Float)
    LH_test = Column(Float)
    MINT_test = Column(Float)
    MTC_test = Column(Float)
    OR_test = Column(Float)
    OSP_test = Column(Float)
    PTT_test = Column(Float)
    PTTEP_test = Column(Float)
    PTTGC_test = Column(Float)
    RATCH_test = Column(Float)
    SAWAD_test = Column(Float)
    SCB_test = Column(Float)
    SCC_test = Column(Float)
    SCGP_test = Column(Float)
    TISCO_test = Column(Float)
    TLI_test = Column(Float)
    TOP_test = Column(Float)
    TRUE_test = Column(Float)
    TTB_test = Column(Float)
    TU_test = Column(Float)
    WHA_test = Column(Float)
    ADVANC_predict = Column(Float)
    AOT_predict = Column(Float)
    AWC_predict = Column(Float)
    BANPU_predict = Column(Float)
    BBL_predict = Column(Float)
    BDMS_predict = Column(Float)
    BEM_predict = Column(Float)
    BGRIM_predict = Column(Float)
    BH_predict = Column(Float)
    BTS_predict = Column(Float)
    CBG_predict = Column(Float)
    CENTEL_predict = Column(Float)
    COM7_predict = Column(Float)
    CPALL_predict = Column(Float)
    CPF_predict = Column(Float)
    CPN_predict = Column(Float)
    CRC_predict = Column(Float)
    DELTA_predict = Column(Float)
    EA_predict = Column(Float)
    EGCO_predict = Column(Float)
    GLOBAL_predict = Column(Float)
    GPSC_predict = Column(Float)
    GULF_predict = Column(Float)
    HMPRO_predict = Column(Float)
    INTUCH_predict = Column(Float)
    IVL_predict = Column(Float)
    KBANK_predict = Column(Float)
    KCE_predict = Column(Float)
    KTB_predict = Column(Float)
    KTC_predict = Column(Float)
    LH_predict = Column(Float)
    MINT_predict = Column(Float)
    MTC_predict = Column(Float)
    OR_predict = Column(Float)
    OSP_predict = Column(Float)
    PTT_predict = Column(Float)
    PTTEP_predict = Column(Float)
    PTTGC_predict = Column(Float)
    RATCH_predict = Column(Float)
    SAWAD_predict = Column(Float)
    SCB_predict = Column(Float)
    SCC_predict = Column(Float)
    SCGP_predict = Column(Float)
    TISCO_predict = Column(Float)
    TLI_predict = Column(Float)
    TOP_predict = Column(Float)
    TRUE_predict = Column(Float)
    TTB_predict = Column(Float)
    TU_predict = Column(Float)
    WHA_predict = Column(Float)

# ---------------- Close & Volume Model ----------------


class MergeClose15T(SET50Base, Base):
    __tablename__ = "merge_close_15t"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeClose15T id={self.id} datetime={self.datetime}>"


class MergeClose1H(SET50Base, Base):
    __tablename__ = "merge_close_1h"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeClose1H id={self.id} datetime={self.datetime}>"


class MergeClose4H(SET50Base, Base):
    __tablename__ = "merge_close_4h"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeClose4H id={self.id} datetime={self.datetime}>"


class MergeClose1D(SET50Base, Base):
    __tablename__ = "merge_close_1d"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeClose1D id={self.id} datetime={self.datetime}>"


class MergeVolume15T(SET50Base, Base):
    __tablename__ = "merge_volume_15t"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeVolume15T id={self.id} datetime={self.datetime}>"


class MergeVolume1H(SET50Base, Base):
    __tablename__ = "merge_volume_1h"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeVolume1H id={self.id} datetime={self.datetime}>"


class MergeVolume4H(SET50Base, Base):
    __tablename__ = "merge_volume_4h"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeVolume4H id={self.id} datetime={self.datetime}>"


class MergeVolume1D(SET50Base, Base):
    __tablename__ = "merge_volume_1d"
    id = Column(Integer, primary_key=True)
    datetime = Column(DATETIME(
        storage_format="%(year)04d-%(month)02d-%(day)02d " +
        "%(hour)02d:%(minute)02d:%(second)02d"
    ), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<MergeVolume1D id={self.id} datetime={self.datetime}>"

# ---------------- ARIMA Model ----------------


class ArimaClose15T(SET50Base, Base):
    __tablename__ = "arima_close_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseArima15T id={self.id}>"


class ArimaClose1H(SET50Base, Base):
    __tablename__ = "arima_close_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseArima1H id={self.id}>"


class ArimaClose4H(SET50Base, Base):
    __tablename__ = "arima_close_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseArima4H id={self.id}>"


class ArimaClose1D(SET50Base, Base):
    __tablename__ = "arima_close_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseArima1d id={self.id}>"


class ArimaVolume15T(SET50Base, Base):
    __tablename__ = "arima_volume_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaVolume15T id={self.id}>"


class ArimaVolume1H(SET50Base, Base):
    __tablename__ = "arima_volume_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaVolume1H id={self.id}>"


class ArimaVolume4H(SET50Base, Base):
    __tablename__ = "arima_volume_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaVolume4H id={self.id}>"


class ArimaVolume1D(SET50Base, Base):
    __tablename__ = "arima_volume_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaVolume1D id={self.id}>"

# ------ Backtest ------


class ArimaCloseBacktest15T(BacktestBase, Base):
    __tablename__ = "arima_close_backtest_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaBacktestClose15T id={self.id}>"


class ArimaCloseBacktest1H(BacktestBase, Base):
    __tablename__ = "arima_close_backtest_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaBacktestClose1H id={self.id}>"


class ArimaCloseBacktest4H(BacktestBase, Base):
    __tablename__ = "arima_close_backtest_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaBacktestClose4H id={self.id}>"


class ArimaCloseBacktest1D(BacktestBase, Base):
    __tablename__ = "arima_close_backtest_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaBacktestClose1D id={self.id}>"

# ------ MSE ERROR ------


class ArimaMSE15T(SET50Base, Base):
    __tablename__ = "arima_mse_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaMSE15t id={self.id}>"


class ArimaMSE1H(SET50Base, Base):
    __tablename__ = "arima_mse_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaMSE1H id={self.id}>"


class ArimaMSE4H(SET50Base, Base):
    __tablename__ = "arima_mse_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaMSE4H id={self.id}>"


class ArimaMSE1D(SET50Base, Base):
    __tablename__ = "arima_mse_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<ArimaMSE1D id={self.id}>"

# ---------------- LSTM Model ----------------


class LSTMClose15T(SET50Base, Base):
    __tablename__ = "lstm_close_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseLSTM15T id={self.id}>"


class LSTMClose1H(SET50Base, Base):
    __tablename__ = "lstm_close_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseLSTM1H id={self.id}>"


class LSTMClose4H(SET50Base, Base):
    __tablename__ = "lstm_close_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseLSTM4H id={self.id}>"


class LSTMClose1D(SET50Base, Base):
    __tablename__ = "lstm_close_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<CloseLSTM1d id={self.id}>"


class LSTMVolume15T(SET50Base, Base):
    __tablename__ = "lstm_volume_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMVolume15T id={self.id}>"


class LSTMVolume1H(SET50Base, Base):
    __tablename__ = "lstm_volume_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMVolume1H id={self.id}>"


class LSTMVolume4H(SET50Base, Base):
    __tablename__ = "lstm_volume_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMVolume4H id={self.id}>"


class LSTMVolume1D(SET50Base, Base):
    __tablename__ = "lstm_volume_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMVolume1D id={self.id}>"

# ------ Backtest ------


class LSTMCloseBacktest15T(BacktestBase, Base):
    __tablename__ = "lstm_close_backtest_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMBacktestClose15T id={self.id}>"


class LSTMCloseBacktest1H(BacktestBase, Base):
    __tablename__ = "lstm_close_backtest_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMBacktestClose1H id={self.id}>"


class LSTMCloseBacktest4H(BacktestBase, Base):
    __tablename__ = "lstm_close_backtest_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMBacktestClose4H id={self.id}>"


class LSTMCloseBacktest1D(BacktestBase, Base):
    __tablename__ = "lstm_close_backtest_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMBacktestClose1D id={self.id}>"

# ------ MSE ERROR ------


class LSTMMSE15T(SET50Base, Base):
    __tablename__ = "lstm_mse_15t"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMMSE15t id={self.id}>"


class LSTMMSE1H(SET50Base, Base):
    __tablename__ = "lstm_mse_1h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMMSE1H id={self.id}>"


class LSTMMSE4H(SET50Base, Base):
    __tablename__ = "lstm_mse_4h"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMMSE4H id={self.id}>"


class LSTMMSE1D(SET50Base, Base):
    __tablename__ = "lstm_mse_1d"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<LSTMMSE1D id={self.id}>"

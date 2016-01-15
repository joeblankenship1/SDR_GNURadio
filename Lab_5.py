#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Lab 5
# Generated: Fri Jan 15 15:19:25 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx

class Lab_5(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Lab 5")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250000
        self.gain = gain = 40
        self.freq = freq = 435e6
        self.audio_rate = audio_rate = 48000
        self.audio_interp = audio_interp = 4

        ##################################################
        # Blocks
        ##################################################
        _gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	label="Gain",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	minimum=0,
        	maximum=90,
        	num_steps=90,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_gain_sizer)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.freq,
        	callback=self.set_freq,
        	label="Frequency",
        	converter=forms.float_converter(),
        )
        self.Add(self._freq_text_box)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=audio_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(freq, 0)
        self.uhd_usrp_sink_0.set_gain(gain, 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate * 1.1),
                decimation=audio_rate * audio_interp,
                taps=None,
                fractional_bw=None,
        )
        self.audio_source_0 = audio.source(audio_rate, "", True)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=audio_rate,
        	quad_rate=audio_rate * audio_interp,
        	tau=75e-6,
        	max_dev=5e3,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_tx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.audio_source_0, 0), (self.analog_nbfm_tx_0, 0))    
        self.connect((self.audio_source_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.uhd_usrp_sink_0, 0))    


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_sink_0.set_gain(self.gain, 0)
        self._gain_slider.set_value(self.gain)
        self._gain_text_box.set_value(self.gain)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_sink_0.set_center_freq(self.freq, 0)
        self._freq_text_box.set_value(self.freq)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.audio_rate)

    def get_audio_interp(self):
        return self.audio_interp

    def set_audio_interp(self, audio_interp):
        self.audio_interp = audio_interp


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = Lab_5()
    tb.Start(True)
    tb.Wait()

#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Lab 4 1
# Generated: Fri Jan 15 15:19:20 2016
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
from gnuradio import blocks
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
import math
import time
import wx

class Lab_4_1(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Lab 4 1")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250e3
        self.gain = gain = 40
        self.freq = freq = 98e6
        self.deviation = deviation = 30e3*0 + 5e3
        self.audio_rate = audio_rate = int(48e3)

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.samp_rate,
        	callback=self.set_samp_rate,
        	label="Sample Rate",
        	converter=forms.float_converter(),
        )
        self.Add(self._samp_rate_text_box)
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
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=audio_rate,
        	v_scale=0.25,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0.set_gain(gain, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=audio_rate,
                decimation=int(samp_rate),
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, audio_rate, 3.5e3, 0.5e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.audio_sink_0 = audio.sink(audio_rate, "", True)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf((audio_rate/(2*math.pi*deviation))* 0 + ((2*math.pi*deviation)/audio_rate))
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(-80, 1e-3, 0, False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.analog_quadrature_demod_cf_0, 0))    
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_pwr_squelch_xx_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.rational_resampler_xxx_0, 0))    


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self._samp_rate_text_box.set_value(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self._gain_slider.set_value(self.gain)
        self._gain_text_box.set_value(self.gain)
        self.uhd_usrp_source_0.set_gain(self.gain, 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_text_box.set_value(self.freq)
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)

    def get_deviation(self):
        return self.deviation

    def set_deviation(self, deviation):
        self.deviation = deviation
        self.analog_quadrature_demod_cf_0.set_gain((self.audio_rate/(2*math.pi*self.deviation))* 0 + ((2*math.pi*self.deviation)/self.audio_rate))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.audio_rate)
        self.analog_quadrature_demod_cf_0.set_gain((self.audio_rate/(2*math.pi*self.deviation))* 0 + ((2*math.pi*self.deviation)/self.audio_rate))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.audio_rate, 3.5e3, 0.5e3, firdes.WIN_HAMMING, 6.76))


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = Lab_4_1()
    tb.Start(True)
    tb.Wait()

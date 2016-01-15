#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Lab 2 1
# Generated: Fri Jan 15 15:18:50 2016
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class Lab_2_1(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Lab 2 1")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.signal_amp = signal_amp = 1
        self.samp_rate = samp_rate = 32000
        self.noise_amp = noise_amp = -130
        self.freq = freq = 1

        ##################################################
        # Blocks
        ##################################################
        _signal_amp_sizer = wx.BoxSizer(wx.VERTICAL)
        self._signal_amp_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_signal_amp_sizer,
        	value=self.signal_amp,
        	callback=self.set_signal_amp,
        	label="Signal Amp",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._signal_amp_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_signal_amp_sizer,
        	value=self.signal_amp,
        	callback=self.set_signal_amp,
        	minimum=0,
        	maximum=2,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_signal_amp_sizer)
        _noise_amp_sizer = wx.BoxSizer(wx.VERTICAL)
        self._noise_amp_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_noise_amp_sizer,
        	value=self.noise_amp,
        	callback=self.set_noise_amp,
        	label="Noise Amp",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._noise_amp_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_noise_amp_sizer,
        	value=self.noise_amp,
        	callback=self.set_noise_amp,
        	minimum=-150,
        	maximum=0,
        	num_steps=150,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_noise_amp_sizer)
        self.nb = self.nb = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "Scope")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "FFT")
        self.Add(self.nb)
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label="Frequency",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=0,
        	maximum=10,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.nb.GetPage(0).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0.5,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=True,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.nb.GetPage(0).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.nb.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.nb.GetPage(1).Add(self.wxgui_fftsink2_0.win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq, signal_amp, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 10.0**(1. * noise_amp / 20.0), 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_scopesink2_0, 0))    


    def get_signal_amp(self):
        return self.signal_amp

    def set_signal_amp(self, signal_amp):
        self.signal_amp = signal_amp
        self.analog_sig_source_x_0.set_amplitude(self.signal_amp)
        self._signal_amp_slider.set_value(self.signal_amp)
        self._signal_amp_text_box.set_value(self.signal_amp)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self._noise_amp_slider.set_value(self.noise_amp)
        self._noise_amp_text_box.set_value(self.noise_amp)
        self.analog_noise_source_x_0.set_amplitude(10.0**(1. * self.noise_amp / 20.0))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_0.set_frequency(self.freq)
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = Lab_2_1()
    tb.Start(True)
    tb.Wait()

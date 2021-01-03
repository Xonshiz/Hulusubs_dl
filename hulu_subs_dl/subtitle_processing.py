#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def vtt_parsing(vtt_text):
    vtt_text = str(vtt_text).replace(' --&gt; ', ' --> ')
    line_start_time_stamps = []
    line_end_time_stamps = []
    line_properties = []
    actual_lines = []
    # double_line_regex = r'--(.*?)\r\n--(.*?)$'
    double_line_regex = r'--(.*?)--(.*?)$'
    # double_line_regex = re.compile(r"""--(.*?)(\s?)--(.*?)""", re.MULTILINE)
    regex = re.compile(r"""(^[0-9]{2}[:][0-9]{2}[:][0-9]{2}[.,][0-9]{3})   
                             [ ]-->[ ]                                     
                             ([0-9]{2}[:][0-9]{2}[:][0-9]{2}[.,][0-9]{3})  
                             (.*)\r?\n([\s\S]*?)\s*(?:(?:\r?\n){2}|\Z)""", re.MULTILINE | re.VERBOSE)
    subtitle_match_count = 0
    for match in regex.finditer(vtt_text):
        subtitle_match_count += 1
        group1, group2, group3, group4 = match.groups()
        line_start_time_stamps.append(group1.strip())
        line_end_time_stamps.append(group2.strip())
        # line_properties.append(group3.strip())
        # actual_lines.append(group4.strip())
        group4 = group4.replace('\r', '\\r').replace('\n', '\\n')
        double_line_search = re.search(double_line_regex, group4.strip())
        # _double_line_search = re.search(double_line_regex, group4.strip())
        # _double_line_search_ = re.findall(double_line_regex, group4.strip())
        if group1.strip() == "00:06:22.208":
            print("FOUND!")
        if double_line_search:
            if group1.strip() == "00:06:22.208":
                print("FOUND!")
            dub_ = double_line_search.group(0).strip()
            _dub_ = double_line_search.groups()
            dub_one = double_line_search.group(1).strip()
            dub_two = double_line_search.group(2).strip()
            line_properties.append('align:middle line:7%')
            actual_lines.append(vtt_line_cleaner(double_line_search.group(1).replace('\\r', '').replace('\\n', '\n')))
            line_start_time_stamps.append(group1.strip())
            line_end_time_stamps.append(group2.strip())
            line_properties.append(group3.strip())
            actual_lines.append(vtt_line_cleaner(double_line_search.group(2).replace('\\r', '').replace('\\n', '\n')))
            print('Two Lines')
        else:
            line_properties.append(group3.strip())
            actual_lines.append(vtt_line_cleaner(group4.replace('\r', '').replace('\\r', '').replace('\\n', '\n').strip()))
    return line_start_time_stamps, line_end_time_stamps, line_properties, actual_lines


def vtt_line_cleaner(line_content):
    if line_content:
        return str(line_content.encode('utf-8')).replace('--', '').strip()
    return line_content


def line_format_srt(idx, starting_stamp, ending_stamp, content, position_style):
    """
    \an8
    34
    00:01:38,820 --> 00:01:43,330
    <font size="20"><b><i>A new horizon, look, how far you've come</i></b></font>
    :return:
    """
    format_string = '{0}\n{1} --> {2}\n<font size="30">{4}{3}</font>\n\n'.format(idx, starting_stamp, ending_stamp, content, position_style)
    return format_string


def line_format_ass(starting_stamp, ending_stamp, style, content):
    """
    Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
    Dialogue: 0,0:01:41.54,0:01:43.08,Default,,0,0,0,,Hero,
    :return:
    """
    format_string = 'Dialogue: 0,{0},{1},{2},,0,0,0,,{3}\n'.format(starting_stamp, ending_stamp, style, str(content).replace('\n', '\N'))
    return format_string


def time_formatter_srt(timestamp):
    # VTT Timestamp : 00:01:43.083
    # SRT Timestamp : 00:01:43,083
    formatted_ts = timestamp
    regex_ts_pattern = r'(.*?):(.*?):(.*?).([\d]{3})'
    regex_search = re.search(regex_ts_pattern, str(timestamp))
    if regex_search:
        formatted_ts = '{0}:{1}:{2},{3}'.format(regex_search.group(1).strip(), regex_search.group(2).strip(),
                                                regex_search.group(3).strip(), regex_search.group(4).strip())
    return formatted_ts


def time_formatter_ass(timestamp):
    # VTT Timestamp : 00:01:43.083
    # ASS Timestamp : 0:01:43.08
    formatted_ts = timestamp
    regex_ts_pattern = r'(.*?):(.*?):(.*?).([\d]{3})'
    regex_search = re.search(regex_ts_pattern, str(timestamp))
    if regex_search:
        formatted_ts = '{0}:{1}:{2}.{3}'.format(regex_search.group(1).strip()[1:], regex_search.group(2).strip(),
                                                regex_search.group(3).strip(), regex_search.group(4).strip()[:2])
    return formatted_ts


def properties_extractor(property_text):
    line_property = None
    align_property = None
    line_regex = r'line:(.*?)%'
    align_regex = r'align:(.*?)%'
    line_exist = re.search(line_regex, str(property_text))
    align_exist = re.search(align_regex, str(property_text))
    if line_exist:
        line_property = line_exist.group(1)
    if align_exist:
        align_property = align_exist.group(1)
    return line_property, align_property


def get_style_value_srt(line=None):
    if line:
        return "{\\an8}"
    else:
        return ""


def get_style_value_ass(align='middle', line=None):
    if line:
        return "Top"
    else:
        if align == 'middle':
            return "Default"
        else:
            return "Default"


def convert_vtt_to_ass(vtt_content, need_ending_ts=False):
    locked_index = None
    starting_ts, ending_ts, properties, lines = vtt_parsing(vtt_text=vtt_content)
    if need_ending_ts:
        return ending_ts[-1]
    ass_script_info = "[Script Info]\n; Script generated by Aegisub 3.2.2\n; http://www.aegisub.org/\nScriptType: v4.00+\nPlayResX: 384\nPlayResY: 288\n"
    ass_style_header = "\n[V4+ Styles]\n"
    ass_format = "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
    ass_style = "Style: Default,Arial,16,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,1,0,2,10,10,10,0\n"
    ass_style += "Style: Top,Arial,16,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,1,0,8,10,10,10,0\n"
    ass_event_header = "\n[Events]\n"
    ass_event_format = "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    ass_dialogues = ""
    if len(starting_ts) == len(ending_ts) and len(properties) == len(lines) and len(starting_ts) == len(lines):
        # print("Lengths : \n")
        # print("starting_ts : {0}".format(len(starting_ts)))
        # print("ending_ts : {0}".format(len(ending_ts)))
        # print("properties : {0}".format(len(properties)))
        # print("lines : {0}".format(len(lines)))
        for _idx, line in enumerate(lines):
            if line:
                line_prop, align_prop = properties_extractor(properties[_idx])
                ass_dialogues += line_format_ass(starting_stamp=time_formatter_ass(starting_ts[_idx]),
                                                 ending_stamp=time_formatter_ass(ending_ts[_idx]),
                                                 style=get_style_value_ass(line=line_prop, align=align_prop),
                                                 content=lines[_idx])
            else:
                pass

    subtitle_string = ""
    subtitle_string += ass_script_info
    subtitle_string += ass_style_header
    subtitle_string += ass_format
    subtitle_string += ass_style
    subtitle_string += ass_event_header
    subtitle_string += ass_event_format
    subtitle_string += ass_dialogues
    return subtitle_string


def convert_vtt_to_srt(vtt_content):
    starting_ts, ending_ts, properties, lines = vtt_parsing(vtt_text=vtt_content)
    srt_dialogues = ""
    if len(starting_ts) == len(ending_ts) and len(properties) == len(lines) and len(starting_ts) == len(lines):
        for _idx, line in enumerate(lines):
            if line:
                line_prop, align_prop = properties_extractor(properties[_idx])
                # _idx + 1 because this is line number for SRT, which starts from 1, not 0.
                srt_dialogues += line_format_srt(idx=_idx + 1, starting_stamp=time_formatter_srt(starting_ts[_idx]), ending_stamp=time_formatter_srt(ending_ts[_idx]), content=lines[_idx], position_style=get_style_value_srt(line=line_prop))

    return srt_dialogues


# def write_sub_file(file_location, content_buffer):
#     try:
#         with open(file_location, 'wb') as write_file:
#             write_file.write(str(content_buffer))
#             write_file.flush()
#         return True
#     except Exception as WriteException:
#         print("Couldn't Write File!")
#         return False

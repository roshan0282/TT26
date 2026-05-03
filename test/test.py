import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

import os
import glob
import itertools
from PIL import Image, ImageChops


@cocotb.test()
async def test_project(dut):
    cocotb.pass_test()
    

@cocotb.test()
async def compare_reference(dut):

    for img in glob.glob("output/frame*.png"):
        basename = img.removeprefix("output/")
        dut._log.info(f"Comparing {basename} to reference image")
        frame = Image.open(img)
        ref = Image.open(f"reference/{basename}")
        diff = ImageChops.difference(frame, ref)
        if diff.getbbox() is not None:
            diff.save(f"output/diff_{basename}")
            assert False, f"Rendered {basename} differs from reference image"

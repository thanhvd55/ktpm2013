/*FILE: Test Phương trình bậc 1
 * Author: Vũ Đức Thành
 * MSSV: 10020322
 */
import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class GIAIPTB1Test {
	private GIAIPTB1 giaiPTB1;

	@Before
	public void setUp() throws Exception {
		giaiPTB1 = new GIAIPTB1();
	}

	/*
	 * Test 1
	 * a = 1
	 * b = 1
	 * KQ = 1
	 */
	@Test
	public void Test1() {
		assertEquals(1.0, giaiPTB1.getKQ(1, 1), 0f);
	}

	/*
	 * Test 2
	 * a = 10
	 * b = -90
	 * KQ = 1
	 */
	
	@Test
	public void Test2() {
		assertEquals(-9.0, giaiPTB1.getKQ(10, -90), 0f);
	}
	
	/*
	 * Test 3
	 * a = 0
	 * b = -90
	 * KQ = NULL
	 */
	
	@Test
	public void Test3() {
		assertNotSame(null, giaiPTB1.getKQ(0, -90));
	}
}

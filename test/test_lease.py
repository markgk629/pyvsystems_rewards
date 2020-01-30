from pyvsystems_rewards.lease import Lease


def test_ongoing_lease_is_active():
    lease = Lease('lease_id', 'address', 100000000, 10)
    assert lease.is_active(9) == False
    assert lease.is_active(10) == True
    assert lease.is_active(11) == True

def test_closed_lease_is_active():
    lease = Lease('lease_id', 'address', 100000000, 10, 20)
    assert lease.is_active(9) == False
    assert lease.is_active(10) == True
    assert lease.is_active(19) == True
    assert lease.is_active(20) == False
    assert lease.is_active(21) == False

    # def get_mab(self, height):
    #     if not self.is_active(height):
    #         return None

    #     mab_modifier = (height - self.start_height) / float(self.MAB_MATURES_AFTER_BLOCKS)
    #     mab_modifier = min(1.0, mab_modifier)
    #     return mab_modifier * self.amount

def test_get_mab():
    lease = Lease('lease_id', 'address', 100000000, 10, 10 + Lease.MAB_MATURES_AFTER_BLOCKS + 10)

    # need to write this
    assert False